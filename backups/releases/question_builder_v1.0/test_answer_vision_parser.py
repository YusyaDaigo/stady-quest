from pathlib import Path

from parsers.answer_vision_parser import parse_required_answers_with_vision


answers = parse_required_answers_with_vision(
    answer_pdf_path=Path("source_materials/pharmacy/required/pdf/110_answers.pdf"),
    exam_number=110,
)

print("抽出数:", len(answers))

for i in range(1, 11):
    print(
        i,
        "表示:",
        answers[i]["answer"] + 1,
        "内部:",
        answers[i]["answer"],
    )