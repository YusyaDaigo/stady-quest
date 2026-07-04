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

    return {
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

def escape_js(text: str) -> str:
    if not text:
        return ""

    text = " ".join(text.split())
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("/", "/")

    return text