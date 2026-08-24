from typing import List, Optional

from explanations.explanation_reader import extract_questions_from_js


def validate_exam_import(
    target_file,
    exam_number: int,
    expected_count: int = 90,
    start_question: int = 1,
    excluded_numbers: Optional[List[int]] = None,
):
    if excluded_numbers is None:
        excluded_numbers = []

    text = target_file.read_text(encoding="utf-8")
    questions = extract_questions_from_js(text)

    imported_numbers = sorted(
        question["sourceNumber"]
        for question in questions
        if question["examNumber"] == exam_number
    )

    unique_numbers = sorted(set(imported_numbers))

    duplicates = sorted(
        number
        for number in unique_numbers
        if imported_numbers.count(number) > 1
    )

    end_question = start_question + expected_count - 1

    expected_numbers = [
        number
        for number in range(
            start_question,
            end_question + 1,
        )
        if number not in excluded_numbers
    ]

    missing_numbers = [
        number
        for number in expected_numbers
        if number not in unique_numbers
    ]

    extra_numbers = [
        number
        for number in unique_numbers
        if number not in expected_numbers
        and number not in excluded_numbers
    ]

    generated_expected_numbers = [
        number
        for number in unique_numbers
        if number in expected_numbers
    ]

    effective_expected_count = len(expected_numbers)

    print("==============================")
    print(f"Exam      : {exam_number}")
    print(f"Range     : {start_question}-{end_question}")
    print(
        "Excluded  : "
        f"{excluded_numbers if excluded_numbers else 'None'}"
    )
    print(f"Expected  : {effective_expected_count}")
    print(f"Generated : {len(generated_expected_numbers)}")
    print(
        "Missing   : "
        f"{missing_numbers if missing_numbers else 'None'}"
    )
    print(
        "Duplicate : "
        f"{duplicates if duplicates else 'None'}"
    )
    print(
        "Extra     : "
        f"{extra_numbers if extra_numbers else 'None'}"
    )
    print("==============================")

    return {
        "examNumber": exam_number,
        "startQuestion": start_question,
        "endQuestion": end_question,
        "excluded": excluded_numbers,
        "expected": effective_expected_count,
        "generated": len(generated_expected_numbers),
        "missing": missing_numbers,
        "duplicates": duplicates,
        "extra": extra_numbers,
        "ok": (
            len(generated_expected_numbers)
            == effective_expected_count
            and not missing_numbers
            and not duplicates
            and not extra_numbers
        ),
    }
