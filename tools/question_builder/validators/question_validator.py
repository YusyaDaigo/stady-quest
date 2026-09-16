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
    1問の妥当性をチェックする。

    answerは以下の両方を許可する。
    ・単一正答: int
    ・複数正答: list[int]

    正答番号は0始まり。
    """

    for field in REQUIRED_FIELDS:
        if field not in question:
            raise ValueError(
                f"必須項目がありません: {field}"
            )

    choices = question["choices"]
    answer = question["answer"]

    if not isinstance(choices, list):
        raise ValueError(
            "choicesはリストである必要があります"
        )

    if len(choices) < 2:
        raise ValueError(
            "choicesは2つ以上必要です"
        )

    if answer is None:
        if (
            question.get("scoringStatus")
            != "no_answer"
        ):
            raise ValueError(
                "answer=None は "
                "scoringStatus=no_answer の"
                "問題だけ許可されます"
            )

        return True

    if isinstance(answer, int):
        answers = [answer]

    elif isinstance(answer, list):
        if not answer:
            raise ValueError(
                "複数正答のanswerを空にはできません"
            )

        if not all(isinstance(value, int) for value in answer):
            raise ValueError(
                "複数正答のanswerは整数のリストである必要があります"
            )

        if len(answer) != len(set(answer)):
            raise ValueError(
                "answerに同じ正答番号が重複しています"
            )

        answers = answer

    else:
        raise ValueError(
            "answerは整数または整数のリストである必要があります"
        )

    for value in answers:
        if value < 0:
            raise ValueError(
                "answerの番号は0以上である必要があります"
            )

        if value >= len(choices):
            raise ValueError(
                "answerの番号がchoices数を超えています"
            )

    return True
