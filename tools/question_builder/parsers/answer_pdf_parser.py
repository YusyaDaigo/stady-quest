import re

from parsers.pdf_parser import extract_pdf_text


def parse_required_answers_from_pdf(pdf_path):
    text = extract_pdf_text(pdf_path)

    answers = {}

    pattern = re.compile(
        r"(\d{1,3})\s+(物理|化学|生物|衛生|薬理|薬剤|病態|法規|実務)\s+(\d)"
    )

    for match in pattern.finditer(text):
        question_no = int(match.group(1))
        field = match.group(2)
        answer = int(match.group(3)) - 1

        if 1 <= question_no <= 90:
            answers[question_no] = {
                "field": field,
                "answer": answer,
            }

    return answers