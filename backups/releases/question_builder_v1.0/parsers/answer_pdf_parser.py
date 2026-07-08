import re

from parsers.pdf_parser import extract_pdf_text


def parse_required_answers_from_pdf(pdf_path):
    text = extract_pdf_text(pdf_path)

    answers = parse_with_subject_names(text)

    if len(answers) >= 90:
        return answers

    print("⚠️ 科目名Parserで90問抽出できませんでした")
    print("🔁 数字Parserに切り替えます")

    answers = parse_with_number_patterns(text)

    return answers


def parse_with_subject_names(text: str):
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


def parse_with_number_patterns(text: str):
    answers = {}

    # PDF文字化け時でも残りやすい形式:
    # 1xxxx 1
    # 2xxxx 3
    # 6xxxx 4 36xxxx 1
    # のように「問番号 + 文字列 + 正答数字」が並ぶ
    pattern = re.compile(
        r"(?<!\d)(\d{1,2})[^\d\n]{1,20}\s+([1-5])(?=\s|\n)"
    )

    for match in pattern.finditer(text):
        question_no = int(match.group(1))
        answer = int(match.group(2)) - 1

        if 1 <= question_no <= 90 and question_no not in answers:
            answers[question_no] = {
                "field": "",
                "answer": answer,
            }

    return answers