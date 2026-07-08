from pathlib import Path

from formatters.js_formatter import escape_js_text


def update_explanation_by_source_number(
    target_file: Path,
    exam_number: int,
    source_number: int,
    explanation: str,
):
    text = target_file.read_text(encoding="utf-8")

    exam_pattern = f"examNumber: {exam_number},"
    source_pattern = f"sourceNumber: {source_number},"

    exam_index = text.find(exam_pattern)

    if exam_index == -1:
        raise ValueError(f"examNumberが見つかりません: {exam_number}")

    source_index = text.find(source_pattern, exam_index)

    if source_index == -1:
        raise ValueError(f"sourceNumberが見つかりません: {source_number}")

    explanation_pattern = 'explanation:\n      ""'

    explanation_index = text.find(explanation_pattern, source_index)

    if explanation_index == -1:
        raise ValueError(
            f"空のexplanationが見つかりません: 第{exam_number}回 問{source_number}"
        )

    safe_explanation = escape_js_text(explanation)

    replacement = f'explanation:\n      "{safe_explanation}"'

    updated_text = (
        text[:explanation_index]
        + replacement
        + text[explanation_index + len(explanation_pattern):]
    )

    target_file.write_text(updated_text, encoding="utf-8")

    return True