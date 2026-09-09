def build_question_from_vision_result(
    vision_result: dict,
    answer_data: dict,
    exam: str,
    category: str,
    exam_number: int = 111,
):
    question_no = vision_result["question_no"]

    if question_no not in answer_data:
        raise ValueError(
            f"解答データが見つかりません: 問{question_no}"
        )

    answer_info = answer_data[question_no]

    question = {
        "subject": exam,
        "category": category.upper(),

        "sourceType": "past_exam",
        "examNumber": exam_number,
        "sourceNumber": question_no,

        "field": answer_info["field"],

        "question": vision_result["question"],
        "choices": vision_result["choices"],
        "answer": answer_info["answer"],
        "explanation": "",
    }

    required_selections = answer_info.get(
        "requiredSelections"
    )

    if required_selections is not None:
        question[
            "requiredSelections"
        ] = required_selections

    case_id = vision_result.get("case_id")
    case_context = vision_result.get("case_context")

    if case_id:
        question["caseId"] = case_id

    if case_context:
        question["caseContext"] = case_context

    if vision_result.get("has_image"):
        question["hasImage"] = True
        question["image"] = (
            f"/pharmacy/{exam_number}/{category}/q{question_no}.png"
        )

    return question