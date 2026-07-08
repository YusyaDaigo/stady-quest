from explanations.openai_explanation_generator import generate_explanation


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

print(explanation)