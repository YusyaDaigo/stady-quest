from explanations.explanation_reader import extract_questions_from_js


def validate_exam_import(
    target_file,
    exam_number: int,
    expected_count: int = 90,
):
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

    expected_numbers = list(range(1, expected_count + 1))

    missing_numbers = [
        number
        for number in expected_numbers
        if number not in unique_numbers
    ]

    extra_numbers = [
        number
        for number in unique_numbers
        if number not in expected_numbers
    ]

    print("==============================")
    print(f"Exam      : {exam_number}")
    print(f"Expected  : {expected_count}")
    print(f"Generated : {len(unique_numbers)}")
    print(f"Missing   : {missing_numbers if missing_numbers else 'None'}")
    print(f"Duplicate : {duplicates if duplicates else 'None'}")
    print(f"Extra     : {extra_numbers if extra_numbers else 'None'}")
    print("==============================")

    return {
        "examNumber": exam_number,
        "expected": expected_count,
        "generated": len(unique_numbers),
        "missing": missing_numbers,
        "duplicates": duplicates,
        "extra": extra_numbers,
        "ok": (
            len(unique_numbers) == expected_count
            and not missing_numbers
            and not duplicates
            and not extra_numbers
        ),
    }