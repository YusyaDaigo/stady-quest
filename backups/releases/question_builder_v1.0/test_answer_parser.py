from pathlib import Path

from parsers.answer_pdf_parser import parse_required_answers_from_pdf


pdf_path = Path("source_materials/pharmacy/required/pdf/111_answers.pdf")

answers = parse_required_answers_from_pdf(pdf_path)

print(f"抽出数: {len(answers)}")

for question_no in sorted(answers.keys())[:10]:
    print(question_no, answers[question_no])