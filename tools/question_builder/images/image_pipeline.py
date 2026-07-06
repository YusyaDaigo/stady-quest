from pathlib import Path

from explanations.explanation_reader import extract_questions_from_js
from parsers.pdf_image_exporter import export_pdf_pages_to_images
from vision.vision_factory import get_vision_engine
from pipelines.past_exam_pipeline import copy_question_image


def insert_image_metadata(
    target_file: Path,
    exam_number: int,
    source_number: int,
    image_path: str,
):
    text = target_file.read_text(encoding="utf-8")

    source_pattern = f"sourceNumber: {source_number},"
    source_index = text.find(source_pattern)

    if source_index == -1:
        raise ValueError(f"sourceNumberが見つかりません: {source_number}")

    has_image_pattern = "hasImage: true,"
    next_source_index = text.find("sourceNumber:", source_index + 1)

    target_block = (
        text[source_index:next_source_index]
        if next_source_index != -1
        else text[source_index:]
    )

    if has_image_pattern in target_block:
        print(f"⚠️ 画像メタデータ既存: 問{source_number}")
        return False

    field_line_end = text.find("\n", source_index)
    field_index = text.find("field:", source_index)

    if field_index == -1:
        raise ValueError(f"fieldが見つかりません: 問{source_number}")

    insert_pos = text.find("\n", field_index) + 1

    metadata = (
        f'    hasImage: true,\n'
        f'    image: "{image_path}",\n'
    )

    updated_text = (
        text[:insert_pos]
        + metadata
        + text[insert_pos:]
    )

    target_file.write_text(updated_text, encoding="utf-8")

    return True


def run_image_pipeline(
    target_file: Path,
    question_pdf_path: Path,
    exam: str,
    category: str,
    exam_number: int,
    start_number: int = 1,
    end_number: int = 20,
    vision_engine_name: str = "openai",
):
    text = target_file.read_text(encoding="utf-8")
    questions = extract_questions_from_js(text)

    target_questions = [
        question
        for question in questions
        if question["examNumber"] == exam_number
        and start_number <= question["sourceNumber"] <= end_number
    ]

    if not target_questions:
        print("⏭️ 対象問題がありません")
        return False

    image_output_dir = Path(
        f"source_materials/{exam}/{category}/images/{exam_number}"
    )

    image_paths = export_pdf_pages_to_images(
        pdf_path=question_pdf_path,
        output_dir=image_output_dir,
        max_pages=100,
    )

    vision_engine = get_vision_engine(vision_engine_name)

    updated_count = 0

    completed = False

    for image_path in image_paths:
        if completed:
            break

        print(f"📄 画像判定中: {image_path}")

        vision_results = vision_engine(image_path)

        page_question_numbers = [
            result["question_no"]
            for result in vision_results
            if start_number <= result["question_no"] <= end_number
        ]

        if not page_question_numbers:
            continue

        if max(page_question_numbers) >= end_number:
            completed = True

        for index, vision_result in enumerate(vision_results):
            question_no = vision_result["question_no"]

            if not (
                start_number <= question_no <= end_number
            ):
                continue

            if not vision_result.get("has_image"):
                print(f"テキストのみ: 問{question_no}")
                continue

            copied_path = copy_question_image(
                image_path=image_path,
                exam=exam,
                category=category,
                exam_number=exam_number,
                source_number=question_no,
                question_index=index + 1,
                question_count=len(vision_results),
            )

            app_image_path = (
                f"/{exam}/{exam_number}/{category}/q{question_no}.png"
            )

            updated = insert_image_metadata(
                target_file=target_file,
                exam_number=exam_number,
                source_number=question_no,
                image_path=app_image_path,
            )

            if updated:
                updated_count += 1
                print(f"✅ 画像メタデータ追加: 問{question_no}")

    print(f"🖼️ 画像メタデータ追加数: {updated_count}")

    return True