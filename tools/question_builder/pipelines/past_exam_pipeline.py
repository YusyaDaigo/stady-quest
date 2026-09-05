import shutil
from pathlib import Path

from parsers.answer_pdf_parser import parse_answers_from_pdf
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
from vision.openai_vision import analyze_question_across_page_set
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


def needs_multi_page_analysis(
    vision_result: dict,
) -> bool:
    """
    単ページVision結果だけでは問題が完結していない
    可能性がある場合にTrueを返す。

    対象:
    - 選択肢が不足している問題
    - 前問・前ページの情報を参照する問題
    - 下線部や空欄など、単ページ内に対応箇所が
      存在しない可能性がある問題
    """
    choices = vision_result.get("choices", [])
    question = vision_result.get("question", "")

    if (
        not isinstance(choices, list)
        or len(choices) < 2
    ):
        return True

    if not isinstance(question, str):
        return False

    reference_markers = (
        "前問",
        "前の問題",
        "前ページ",
        "この定量法",
        "この方法",
        "この操作",
        "この反応",
        "この実験",
        "この図",
        "この表",
    )

    if any(
        marker in question
        for marker in reference_markers
    ):
        return True

    choices_text = "\n".join(
        str(choice)
        for choice in choices
    )

    dependent_markers = (
        "下線部",
        "空欄",
    )

    if any(
        marker in choices_text
        for marker in dependent_markers
    ):
        return True

    return False

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
    part: int = None,
    vision_engine_name: str = "openai",
    answer_parser: str = "text",
    start_page: int = 2,
    max_pages: int = 2,
):

    question_ranges = {
        "required": (1, 90),
        "theory": (91, 195),
        "practical": (196, 345),
    }

    min_question_no, max_question_no = question_ranges[category]

    if exam == "pharmacy":
        target_file = (
            EXAM_PATHS[exam]
            / f"{category}_{exam_number}.js"
        )

        export_names = {
            "required": f"required{exam_number}Questions",
            "theory": f"theory{exam_number}Questions",
            "practical": f"practical{exam_number}Questions",
        }

        export_name = export_names[category]

        if not target_file.exists():
            target_file.write_text(
                f'import {{ CATEGORIES }} from "./categories";\n\n'
                f'export const {export_name} = [\n\n'
                f'  // AI_QUESTION_INSERT_HERE\n'
                f'];\n',
                encoding="utf-8",
            )
    else:
        target_file = (
            EXAM_PATHS[exam]
            / QUESTION_FILES[category]
        )

    if part is None:
        image_output_dir = Path(
            f"source_materials/{exam}/{category}/images/{exam_number}"
        )
    else:
        image_output_dir = Path(
            f"source_materials/{exam}/{category}/images/"
            f"{exam_number}/part_{part}"
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
        answer_data = parse_answers_from_pdf(
            pdf_path=answer_pdf_path,
            category=category,
        )
    vision_engine = get_vision_engine(vision_engine_name)

    text = target_file.read_text(encoding="utf-8")
    blocks = []

    processed_questions = set()
    case_context_candidates = {}

    for page_index, image_path in enumerate(target_image_paths):
        print(f"📄 解析中: {image_path}")

        vision_results = vision_engine(
            image_path,
            category=category,
        )

        try:
            figure_bboxes = detect_question_bboxes(
                image_path,
                category=category,
            )
        except Exception as e:
            print(f"⚠️ bbox検出失敗 fallback使用: {e}")
            figure_bboxes = {}

        for index, vision_result in enumerate(vision_results):
            question_no = vision_result.get("question_no")

            choices = vision_result.get("choices", [])
            has_image = bool(
                vision_result.get("has_image", False)
            )

            if category == "practical":
                candidate_question = vision_result.get("question", "")

                if (
                    isinstance(question_no, int)
                    and isinstance(choices, list)
                    and len(choices) < 2
                    and isinstance(candidate_question, str)
                    and candidate_question.strip()
                ):
                    case_context_candidates[question_no] = (
                        candidate_question.strip()
                    )

                    print(
                        "📋 caseContext候補保存: "
                        f"問{question_no}"
                    )

            if (
                isinstance(question_no, int)
                and needs_multi_page_analysis(
                    vision_result
                )
            ):
                page_set = []

                previous_index = page_index - 1

                if previous_index >= 0:
                    page_set.append(
                        target_image_paths[previous_index]
                    )

                page_set.append(image_path)

                next_index = page_index + 1

                if next_index < len(target_image_paths):
                    page_set.append(
                        target_image_paths[next_index]
                    )

                if len(page_set) >= 2:
                    try:
                        merged_result = (
                            analyze_question_across_page_set(
                                image_paths=page_set,
                                question_no=question_no,
                                category=category,
                            )
                        )

                        if merged_result is not None:
                            merged_choices = merged_result.get(
                                "choices",
                                [],
                            )

                            if (
                                isinstance(merged_choices, list)
                                and len(merged_choices) >= 2
                            ):
                                print(
                                    "🧩 複数ページ統合成功: "
                                    f"問{question_no} "
                                    f"({len(page_set)}ページ)"
                                )

                                vision_result = merged_result

                    except Exception as e:
                        print(
                            "⚠️ 複数ページVision失敗: "
                            f"問{question_no}: {e}"
                        )

            question_no = vision_result.get("question_no")

            if category == "practical":
                case_context = (
                    case_context_candidates.get(question_no)
                )

                if (
                    isinstance(question_no, int)
                    and case_context
                ):
                    pair_start = (
                        196
                        + ((question_no - 196) // 2) * 2
                    )

                    vision_result = dict(vision_result)
                    vision_result['case_id'] = (
                        f"{exam_number}-"
                        f"{pair_start}-"
                        f"{pair_start + 1}"
                    )
                    vision_result['case_context'] = (
                        case_context
                    )

                    print(
                        "🧩 caseContext付与: "
                        f"問{question_no} → "
                        f"{vision_result['case_id']}"
                    )

            if (
                not isinstance(question_no, int)
                or not (min_question_no <= question_no <= max_question_no)
            ):
                print(f"⚠️ 問番号スキップ: {question_no}")
                continue

            if question_no not in answer_data:
                print(f"⚠️ 解答データなしスキップ: 第{exam_number}回 問{question_no}")
                continue

            if question_no in processed_questions:
                print(
                    f"⏭️ 同一実行内スキップ: 問{question_no}"
                )
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
                processed_questions.add(question_no)

                print(
                    f"⚠️ 同一年度・同一問番号スキップ: 第{exam_number}回 問{question['sourceNumber']}"
                )
                continue

            print(f"🧠 解説生成中: 問{question['sourceNumber']}")

            explanation = generate_explanation(question)
            question["explanation"] = explanation

            blocks.append(build_question_block(question))
            print(f"✅ 追加予定: 問{question['sourceNumber']}")

            processed_questions.add(question_no)

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
