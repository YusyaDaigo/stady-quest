from pathlib import Path

from parsers.answer_pdf_parser import parse_required_answers_from_pdf
from vision.vision_factory import get_vision_engine
from generators.vision_question_builder import build_question_from_vision_result

from validators.question_validator import validate_question
from checkers.duplicate_checker import is_duplicate_question
from formatters.js_formatter import build_question_block
from exporters.file_exporter import backup_file, insert_question_blocks
from config import EXAM_PATHS, QUESTION_FILES


exam = "pharmacy"
category = "required"

image_path = Path("source_materials/pharmacy/required/images/111_required/page_2.png")
answer_pdf_path = Path("source_materials/pharmacy/required/pdf/111_answers.pdf")

target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

vision_engine = get_vision_engine("openai")
vision_results = vision_engine(image_path)

answer_data = parse_required_answers_from_pdf(answer_pdf_path)

text = target_file.read_text(encoding="utf-8")

blocks = []

for vision_result in vision_results:
    question = build_question_from_vision_result(
        vision_result=vision_result,
        answer_data=answer_data,
        exam=exam,
        category=category,
    )

    validate_question(question)

    if is_duplicate_question(question, text):
        print(f"⚠️ 重複スキップ: 問{question['sourceNumber']} {question['question']}")
        continue

    blocks.append(build_question_block(question))
    print(f"✅ 追加予定: 問{question['sourceNumber']}")

if not blocks:
    print("⏭️ 追加する問題がありません")
else:
    backup_path = backup_file(target_file)
    success = insert_question_blocks(target_file, blocks)

    if success:
        print("✅ Vision由来Questionを追加しました")
        print(f"📄 対象: {target_file}")
        print(f"🛡️ バックアップ: {backup_path}")