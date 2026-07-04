def build_question_from_vision_result(
    vision_result: dict,
    answer_data: dict,
    exam: str,
    category: str,
):
    question_no = vision_result["question_no"]

    if question_no not in answer_data:
        raise ValueError(
            f"解答データが見つかりません: 問{question_no}"
        )

    answer_info = answer_data[question_no]

    return {
        "subject": exam,
        "category": category.upper(),
        "field": answer_info["field"],
        "sourceType": "past_exam",
        "sourceNumber": question_no,
        "question": vision_result["question"],
        "choices": vision_result["choices"],
        "answer": answer_info["answer"],
        "explanation": "",
    }