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
from parsers.answer_vision_parser import parse_required_answers_with_vision


def copy_question_image(
    image_path: Path,
    exam: str,
    category: str,
    exam_number: int,
    source_number: int,
    question_index: int,
    question_count: int,
):
    output_dir = Path(
        f"public/{exam}/{exam_number}/{category}"
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"q{source_number}.png"

    crop_page_by_question_index(
        page_image_path=image_path,
        output_path=output_path,
        question_index=question_index,
        question_count=question_count,
    )

    return output_path

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

        for index, vision_result in enumerate(vision_results):
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
            )

                print(f"🖼️ 画像コピー: {copied_path}")

            validate_question(question)

            if is_duplicate_question(question, text):
                print(
                    f"⚠️ 重複スキップ: 問{question['sourceNumber']}"
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