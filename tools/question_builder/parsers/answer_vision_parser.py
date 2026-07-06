import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL
from parsers.pdf_image_exporter import export_pdf_pages_to_images

load_dotenv()


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def parse_required_answers_with_vision(
    answer_pdf_path: Path,
    exam_number: int,
):
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    output_dir = Path(
        f"source_materials/pharmacy/required/answer_images/{exam_number}"
    )

    image_paths = export_pdf_pages_to_images(
        pdf_path=answer_pdf_path,
        output_dir=output_dir,
        max_pages=3,
    )

    client = OpenAI()

    answers = {}

    for image_path in image_paths:
        print(f"📄 解答表解析中: {image_path}")

        prompt = """
薬剤師国家試験の正答表画像です。

必須問題の問1〜問90について、問番号と正答のみを抽出してください。

必ずJSONのみで返してください。

形式:
[
  {"question_no": 1, "answer": 1},
  {"question_no": 2, "answer": 3}
]

注意:
- answer は選択肢番号そのまま、1〜5で返してください。
- 一般問題は含めないでください。
- 問91以降は無視してください。
- 読み取れない問題は推測せず省略してください。
"""

        response = client.responses.create(
            model=OPENAI_VISION_MODEL,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt},
                        {"type": "input_image", "image_url": image_to_data_url(image_path)},
                    ],
                }
            ],
        )

        data = json.loads(response.output_text)

        if isinstance(data, dict) and "answers" in data:
            data = data["answers"]

        for item in data:
            question_no = int(item["question_no"])
            answer = int(item["answer"])

            if 1 <= question_no <= 90:
                answers[question_no] = {
                    "field": "",
                    "answer": answer - 1,
                }

    return answers