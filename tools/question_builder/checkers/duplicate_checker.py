def is_duplicate_question(question: dict, text: str) -> bool:
    return question["question"] in text