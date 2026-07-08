import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL

load_dotenv()

BBOX_CACHE_DIR = Path(
    "tools/question_builder/cache/pharmacy/required/bboxes"
)


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def get_bbox_cache_path(image_path: Path) -> Path:
    """
    例:
    source_materials/pharmacy/required/images/110/page_14.png
    ↓
    tools/question_builder/cache/pharmacy/required/bboxes/110/page_14.json
    """
    parts = image_path.parts

    try:
      exam_number = parts[parts.index("images") + 1]
    except Exception:
      exam_number = "unknown"

    return BBOX_CACHE_DIR / exam_number / f"{image_path.stem}.json"


def normalize_bbox_result(data):
    if isinstance(data, dict) and "questions" in data:
        data = data["questions"]

    result = {}

    for item in data:
        try:
            question_no = int(item.get("question_no"))
        except Exception:
            continue

        if not (1 <= question_no <= 90):
            continue

        bbox = item.get("figure_bbox")
        has_figure = bool(item.get("has_figure"))

        if (
            has_figure
            and isinstance(bbox, list)
            and len(bbox) == 4
        ):
            result[question_no] = [int(v) for v in bbox]

    return result


def detect_question_bboxes(image_path: Path):
    cache_path = get_bbox_cache_path(image_path)

    if cache_path.exists():
        print(f"📦 bbox cache使用: {cache_path}")
        cached_data = json.loads(
            cache_path.read_text(encoding="utf-8")
        )
        return {
            int(key): value
            for key, value in cached_data.items()
        }

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    client = OpenAI()

    prompt = """
薬剤師国家試験の問題ページ画像です。

このページ内に含まれる各問題について、図・表・化学構造式・グラフなど、問題を解くために必要な画像領域を検出してください。

必ずJSONのみで返してください。

形式:
[
  {
    "question_no": 6,
    "has_figure": true,
    "figure_bbox": [left, top, right, bottom]
  }
]

ルール:
- bboxは画像左上を原点としたピクセル座標で返してください。
- figure_bbox は、図・表・構造式・グラフ・模式図など必要な視覚情報だけを囲んでください。
- 問題文や選択肢の文章は原則として含めないでください。
- ただし、選択肢そのものが図・構造式・表の場合は、その選択肢部分を含めてください。
- 図がない問題は has_figure:false とし、figure_bbox:null にしてください。
- 問番号が読めない場合は省略してください。
- 問1〜問90以外は無視してください。
"""

    response = client.responses.create(
        model=OPENAI_VISION_MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_image",
                        "image_url": image_to_data_url(image_path),
                    },
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    result = normalize_bbox_result(data)

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"💾 bbox cache保存: {cache_path}")

    return result