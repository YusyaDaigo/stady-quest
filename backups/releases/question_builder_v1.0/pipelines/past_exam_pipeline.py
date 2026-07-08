import shutil
from pathlib import Path

from parsers.answer_pdf_parser import parse_required_answers_from_pdf
from parsers.pdf_image_exporter import export_pdf_pages_to_images
from vision.vision_factory import get_vision_engine
from generators.vision_question_builder import build_question_from_vision_result

from validators.question_validator import validate_question
from checkers.duplicate_checker import is_duplicate_question
from formatters.js_formatter import build_question_block
from exporters.file_exporter import backup_file, insert_question_blocks
from config import EXAM_PATHS, QUESTION_FILES

from explanations.openai_explanation_generator import generate_explanation
from explanations.explanation_updater import update_explanation_by_source_number
from images.question_image_cropper import crop_page_by_question_index
from images.vision_bbox_cropper import crop_by_bbox
from vision.openai_bbox_detector import detect_question_bboxes
from parsers.answer_vision_parser import parse_required_answers_with_vision


def copy_question_image(
    image_path: Path,
    exam: str,
    category: str,
    exam_number: int,
    source_number: int,
    question_index: int,
    question_count: int,
    figure_bbox=None,
):
    output_dir = Path(
        f"public/{exam}/{exam_number}/{category}"
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"q{source_number}.png"

    if figure_bbox:
        try:
            crop_by_bbox(
                page_image_path=image_path,
                output_path=output_path,
                bbox=figure_bbox,
            )
            return output_path
        except Exception as e:
            print(
                f"⚠️ bbox crop失敗: 第{exam_number}回 問{source_number}: {e}"
            )

    crop_page_by_question_index(
        page_image_path=image_path,
        output_path=output_path,
        question_index=question_index,
        question_count=question_count,
    )

    return output_path

def is_same_exam_source_number_exists(
    text: str,
    exam_number: int,
    source_number: int,
) -> bool:
    exam_pattern = f"examNumber: {exam_number},"
    source_pattern = f"sourceNumber: {source_number},"

    exam_index = text.find(exam_pattern)

    while exam_index != -1:
        next_exam_index = text.find(
            "examNumber:",
            exam_index + len(exam_pattern)
        )

        block = (
            text[exam_index:next_exam_index]
            if next_exam_index != -1
            else text[exam_index:]
        )

        if source_pattern in block:
            return True

        exam_index = text.find(
            exam_pattern,
            exam_index + len(exam_pattern)
        )

    return False

def run_past_exam_pipeline(
    exam: str,
    category: str,
    exam_number: int,
    question_pdf_path: Path,
    answer_pdf_path: Path,
    vision_engine_name: str = "openai",
    answer_parser: str = "text",
    start_page: int = 2,
    max_pages: int = 2,
):
    if exam == "pharmacy" and category == "required":
        target_file = EXAM_PATHS[exam] / f"required_{exam_number}.js"

        if not target_file.exists():
            target_file.write_text(
                f'import {{ CATEGORIES }} from "./categories";\n\n'
                f'export const required{exam_number}Questions = [\n\n'
                f'  // AI_QUESTION_INSERT_HERE\n'
                f'];\n',
                encoding="utf-8",
            )
    else:
        target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

    image_output_dir = Path(
        f"source_materials/{exam}/{category}/images/{exam_number}"
    )

    image_paths = export_pdf_pages_to_images(
        pdf_path=question_pdf_path,
        output_dir=image_output_dir,
        max_pages=start_page + max_pages - 1,
    )

    target_image_paths = image_paths[start_page - 1:start_page - 1 + max_pages]

    if answer_parser == "vision":
        answer_data = parse_required_answers_with_vision(
            answer_pdf_path=answer_pdf_path,
            exam_number=exam_number,
        )
    else:
        answer_data = parse_required_answers_from_pdf(answer_pdf_path)
    vision_engine = get_vision_engine(vision_engine_name)

    text = target_file.read_text(encoding="utf-8")
    blocks = []

    for image_path in target_image_paths:
        print(f"📄 解析中: {image_path}")

        vision_results = vision_engine(image_path)

        try:
            figure_bboxes = detect_question_bboxes(image_path)
        except Exception as e:
            print(f"⚠️ bbox検出失敗 fallback使用: {e}")
            figure_bboxes = {}

        for index, vision_result in enumerate(vision_results):
            question_no = vision_result.get("question_no")

            if not isinstance(question_no, int) or not (1 <= question_no <= 90):
                print(f"⚠️ 問番号スキップ: {question_no}")
                continue

            if question_no not in answer_data:
                print(f"⚠️ 解答データなしスキップ: 第{exam_number}回 問{question_no}")
                continue

            question = build_question_from_vision_result(
                vision_result=vision_result,
                answer_data=answer_data,
                exam=exam,
                category=category,
                exam_number=exam_number,
            )

            if question.get("hasImage"):
                copied_path = copy_question_image(
                    image_path=image_path,
                    exam=exam,
                    category=category,
                    exam_number=exam_number,
                    source_number=question["sourceNumber"],
                    question_index=index + 1,
                    question_count=len(vision_results),
                    figure_bbox=figure_bboxes.get(question["sourceNumber"]),
            )

                print(f"🖼️ 画像コピー: {copied_path}")

            try:
                validate_question(question)
            except Exception as e:
                print(
                    f"⚠️ 第{exam_number}回 "
                    f"問{question['sourceNumber']} "
                    f"スキップ: {e}"
                )
                continue

            # 過去問取り込みでは、年度違いの類似問題も正規データとして扱うため
            # 問題文ベースの重複チェックは行わない。
            # 類題生成時のみ duplicate_checker を使う。
            # if is_duplicate_question(question, text):
            #     print(
            #         f"⚠️ 重複スキップ: 問{question['sourceNumber']}"
            #     )
            #     continue

            if is_same_exam_source_number_exists(
                text=text,
                exam_number=exam_number,
                source_number=question["sourceNumber"],
            ):
                print(
                    f"⚠️ 同一年度・同一問番号スキップ: 第{exam_number}回 問{question['sourceNumber']}"
                )
                continue

            print(f"🧠 解説生成中: 問{question['sourceNumber']}")

            explanation = generate_explanation(question)
            question["explanation"] = explanation

            blocks.append(build_question_block(question))
            print(f"✅ 追加予定: 問{question['sourceNumber']}")

    if not blocks:
        print("⏭️ 追加する問題がありません")
        return False

    backup_path = backup_file(target_file)
    success = insert_question_blocks(target_file, blocks)

    if success:
        print("✅ Pipeline完了")
        print(f"📄 対象: {target_file}")
        print(f"🛡️ バックアップ: {backup_path}")
        print(f"🧩 追加数: {len(blocks)}")

    return success