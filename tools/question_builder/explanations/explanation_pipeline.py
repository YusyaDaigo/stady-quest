from explanations.explanation_reader import extract_questions_from_js
from explanations.openai_explanation_generator import generate_explanation
from explanations.explanation_updater import update_explanation_by_source_number


def run_explanation_pipeline(
    target_file,
    exam_number: int,
    start_number: int = 1,
    end_number: int = 5,
):
    text = target_file.read_text(encoding="utf-8")

    questions = extract_questions_from_js(text)

    target_questions = [
        question
        for question in questions
        if question["examNumber"] == exam_number
        and start_number <= question["sourceNumber"] <= end_number
        and question["explanation"] == ""
    ]

    print(f"解説生成対象: {len(target_questions)}問")

    for question in target_questions:
        print(f"🧠 解説生成中: 問{question['sourceNumber']}")

        explanation = generate_explanation(question)

        update_explanation_by_source_number(
            target_file=target_file,
            exam_number=exam_number,
            source_number=question["sourceNumber"],
            explanation=explanation,
        )

        print(f"✅ 更新完了: 問{question['sourceNumber']}")