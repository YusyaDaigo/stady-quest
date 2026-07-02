REQUIRED_FIELDS = [
    "subject",
    "category",
    "question",
    "choices",
    "answer",
    "explanation",
]


def validate_question(question: dict):
    """
    1問の妥当性をチェック
    """

    for field in REQUIRED_FIELDS:
        if field not in question:
            raise ValueError(
                f"必須項目がありません: {field}"
            )

    if not isinstance(question["choices"], list):
        raise ValueError(
            "choicesはリストである必要があります"
        )

    if len(question["choices"]) < 2:
        raise ValueError(
            "choicesは2つ以上必要です"
        )

    if question["answer"] >= len(question["choices"]):
        raise ValueError(
            "answerの番号がchoices数を超えています"
        )

    return True