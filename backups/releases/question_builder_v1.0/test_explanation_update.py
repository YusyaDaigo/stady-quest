from pathlib import Path

from explanations.openai_explanation_generator import generate_explanation
from explanations.explanation_updater import update_explanation_by_source_number
from config import EXAM_PATHS, QUESTION_FILES


exam = "pharmacy"
category = "required"
exam_number = 111
source_number = 1

target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

question = {
    "field": "物理",
    "question": "水100 mLに、ある有機溶媒100 mLを加えると二液相が形成され、上層が水相となった。この有機溶媒はどれか。1つ選べ。",
    "choices": [
        "ジエチルエーテル",
        "1-オクタノール",
        "n-ヘキサン",
        "トルエン",
        "クロロホルム",
    ],
    "answer": 4,
}

explanation = generate_explanation(question)

update_explanation_by_source_number(
    target_file=target_file,
    exam_number=exam_number,
    source_number=source_number,
    explanation=explanation,
)

print("✅ 解説を更新しました")
print(explanation)