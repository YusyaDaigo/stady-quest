import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


EXPLANATION_MODEL = "gpt-5.5"


def generate_explanation(question: dict) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    client = OpenAI()

    choices = question["choices"]
    answer = question["answer"]

    choices_text = "\n".join(
        [
            f"{index + 1}. {choice}"
            for index, choice in enumerate(choices)
        ]
    )

    if isinstance(answer, list):
        correct_answers = answer
    else:
        correct_answers = [answer]

    correct_choices_text = "\n".join(
        [
            f"{index + 1}. {choices[index]}"
            for index in correct_answers
        ]
    )

    prompt = f"""
あなたは薬剤師国家試験対策の講師です。

以下の問題について、受験生向けの簡潔で分かりやすい解説を作成してください。

条件:
- 正答の理由を説明する
- 他の選択肢がなぜ違うかも軽く触れる
- 複数正答の場合は、正答となる各選択肢について説明する
- 文章は長すぎず、Study QUESTアプリ内で読める長さにする
- 断定しすぎず、国家試験対策として自然な表現にする
- JSONのみで返す

出力形式:
{{
  "explanation": "解説文"
}}

科目: {question.get("field", "")}

問題:
{question["question"]}

選択肢:
{choices_text}

正答:
{correct_choices_text}
"""

    response = client.responses.create(
        model=EXPLANATION_MODEL,
        input=prompt,
    )

    data = json.loads(response.output_text)

    return data["explanation"]
