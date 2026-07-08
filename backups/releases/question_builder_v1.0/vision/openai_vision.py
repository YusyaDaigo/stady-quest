import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL, PHARMACY_FIELD_ALIASES

load_dotenv()


def normalize_field(field: str) -> str:
    return PHARMACY_FIELD_ALIASES.get(field, field)


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def analyze_page(image_path):
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    client = OpenAI()
    image_path = Path(image_path)
    image_data_url = image_to_data_url(image_path)

    prompt = """
薬剤師国家試験の必須問題ページ画像です。

画像内に見えている問題をすべて抽出してください。

必ずJSONのみで返してください。

形式:
[
  {
    "question_no": 1,
    "field": "物理",
    "question": "問題文",
    "choices": [
      "選択肢1",
      "選択肢2",
      "選択肢3",
      "選択肢4",
      "選択肢5"
    ],
    "has_image": false
  }
]

fieldは次のいずれかに正規化してください:
物理, 化学, 生物, 衛生, 薬理, 薬剤, 病態・薬物治療, 法規・制度・倫理, 実務

has_image は、問題を解くために図、表、グラフ、写真、構造式、波形、模式図などの画像情報が必要な場合は true にしてください。
問題文と選択肢だけで解ける場合は false にしてください。

見えていない問題は作らないでください。
"""

    response = client.responses.create(
        model=OPENAI_VISION_MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": image_data_url},
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    if isinstance(data, dict):
        if "questions" in data:
            questions = data["questions"]
        else:
            questions = [data]
    elif isinstance(data, list):
        questions = data
    else:
        raise ValueError(
            f"OpenAI Visionの返答形式が不正です: {type(data)}"
        )

    normalized_questions = []

    for q in questions:
        if not isinstance(q, dict):
            print(f"⚠️ 不正な問題データをスキップ: {q}")
            continue

        q["field"] = normalize_field(q.get("field", ""))
        q["has_image"] = bool(q.get("has_image", False))

        normalized_questions.append(q)

    return normalized_questions