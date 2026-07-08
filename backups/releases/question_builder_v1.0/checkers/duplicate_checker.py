def is_duplicate_question(question: dict, text: str) -> bool:
    exam_number = question.get("examNumber")
    source_number = question.get("sourceNumber")
    source_type = question.get("sourceType")

    if exam_number is not None and source_number is not None and source_type:
        patterns = [
            f'sourceType: "{source_type}"',
            f"examNumber: {exam_number}",
            f"sourceNumber: {source_number}",
        ]

        if all(pattern in text for pattern in patterns):
            return True

    if question["question"] in text:
        return True

    return False