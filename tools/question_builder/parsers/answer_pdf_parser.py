import re
from pathlib import Path
from typing import Dict, List, Tuple

from parsers.pdf_parser import extract_pdf_text


QUESTION_RANGES = {
    "required": (1, 90),
    "theory": (91, 195),
    "practical": (196, 345),
}


# 公式に「解なし」とされた問題。
# キー: (試験回, カテゴリ)
EXCLUDED_QUESTIONS: Dict[Tuple[int, str], List[int]] = {
    (111, "theory"): [92],
    (111, "practical"): [199, 287],
}


SUBJECTS = (
    "物理",
    "化学",
    "生物",
    "衛生",
    "薬理",
    "薬剤",
    "病態",
    "法規",
    "実務",
)


def extract_exam_number(pdf_path) -> int:
    """
    111_answers.pdf のようなファイル名から試験回を取得する。
    """

    stem = Path(pdf_path).stem

    match = re.search(r"(\d{2,3})", stem)

    if match is None:
        raise ValueError(
            f"PDFファイル名から試験回を取得できません: {pdf_path}"
        )

    return int(match.group(1))


def parse_answers_from_pdf(
    pdf_path,
    category: str = "required",
):
    """
    薬剤師国家試験の公式正答PDFを解析する。

    対応カテゴリ:
    ・required  : 問1〜90
    ・theory    : 問91〜195
    ・practical : 問196〜345

    answerは0始まりで返す。
    単一正答はint、複数正答はlist[int]。
    正答がない問題は辞書へ登録しない。
    """

    if category not in QUESTION_RANGES:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    exam_number = extract_exam_number(pdf_path)
    excluded_numbers = EXCLUDED_QUESTIONS.get(
        (exam_number, category),
        [],
    )

    text = extract_pdf_text(pdf_path)

    answers = parse_with_subject_names(
        text=text,
        category=category,
    )

    start_no, end_no = QUESTION_RANGES[category]

    full_count = end_no - start_no + 1
    expected_count = full_count - len(excluded_numbers)

    print(
        f"📘 解答抽出: {category} "
        f"{len(answers)}/{expected_count}問"
    )

    if excluded_numbers:
        print(
            f"🚫 解なし除外: 第{exam_number}回 "
            f"{excluded_numbers}"
        )

    return answers


def parse_required_answers_from_pdf(pdf_path):
    """
    既存コードとの互換用。
    """

    return parse_answers_from_pdf(
        pdf_path=pdf_path,
        category="required",
    )


def parse_with_subject_names(
    text: str,
    category: str = "required",
):
    answers = {}

    start_no, end_no = QUESTION_RANGES[category]
    subject_pattern = "|".join(SUBJECTS)

    pattern = re.compile(
        rf"(?<!\d)(\d{{1,3}})\s+"
        rf"({subject_pattern})"
        rf"(?:\s+([1-6])(?=\s|$))?"
        rf"(?:\s+([1-6])(?=\s|$))?"
    )

    for match in pattern.finditer(text):
        question_no = int(match.group(1))

        if not start_no <= question_no <= end_no:
            continue

        field = match.group(2)

        raw_answers = [
            value
            for value in (
                match.group(3),
                match.group(4),
            )
            if value is not None
        ]

        # 「解なし」は正答数字が抽出されないため、
        # answer_dataへ登録せずPipeline側でスキップする。
        if not raw_answers:
            continue

        zero_based_answers = [
            int(value) - 1
            for value in raw_answers
        ]

        answer = (
            zero_based_answers[0]
            if len(zero_based_answers) == 1
            else zero_based_answers
        )

        answers[question_no] = {
            "field": field,
            "answer": answer,
        }

    return answers
