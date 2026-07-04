import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

from config import OPENAI_VISION_MODEL, PHARMACY_FIELD_ALIASES


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
{
  "question_no": 1,
  "field": "物理",
  "question": "問題文",
  "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4", "選択肢5"]
}

fieldは次のいずれかに正規化してください:
物理, 化学, 生物, 衛生, 薬理, 薬剤, 病態・薬物治療, 法規・制度・倫理, 実務
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

    questions = json.loads(response.output_text)

    for q in questions:
        q["field"] = normalize_field(q["field"])

    return questions