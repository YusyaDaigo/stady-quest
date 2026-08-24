import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL

load_dotenv()


QUESTION_RANGES = {
    "required": (1, 90),
    "theory": (91, 195),
    "practical": (196, 345),
}


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def get_bbox_cache_path(
    image_path: Path,
    category: str,
) -> Path:
    parts = image_path.parts

    try:
        images_index = parts.index("images")
        exam_number = parts[images_index + 1]
    except Exception:
        exam_number = "unknown"

    part_name = None

    try:
        candidate = parts[images_index + 2]

        if candidate.startswith("part_"):
            part_name = candidate
    except Exception:
        part_name = None

    cache_dir = (
        Path("tools/question_builder/cache/pharmacy")
        / category
        / "bboxes"
        / exam_number
    )

    if part_name is not None:
        cache_dir = cache_dir / part_name

    return cache_dir / f"{image_path.stem}.json"


def normalize_bbox_result(
    data,
    category: str,
):
    if isinstance(data, dict) and "questions" in data:
        data = data["questions"]

    if not isinstance(data, list):
        return {}

    min_question_no, max_question_no = QUESTION_RANGES[category]
    result = {}

    for item in data:
        if not isinstance(item, dict):
            continue

        try:
            question_no = int(item.get("question_no"))
        except (TypeError, ValueError):
            continue

        if not (min_question_no <= question_no <= max_question_no):
            continue

        bbox = item.get("figure_bbox")
        has_figure = bool(item.get("has_figure"))

        if (
            has_figure
            and isinstance(bbox, list)
            and len(bbox) == 4
        ):
            try:
                result[question_no] = [int(value) for value in bbox]
            except (TypeError, ValueError):
                continue

    return result


def detect_question_bboxes(
    image_path: Path,
    category: str = "required",
):
    if category not in QUESTION_RANGES:
        raise ValueError(f"未対応のカテゴリです: {category}")

    cache_path = get_bbox_cache_path(
        image_path=image_path,
        category=category,
    )

    if cache_path.exists():
        print(f"📦 bbox cache使用: {cache_path}")
        cached_data = json.loads(
            cache_path.read_text(encoding="utf-8")
        )
        return {
            int(key): value
            for key, value in cached_data.items()
        }

    no_api = os.getenv("STUDY_QUEST_NO_API") == "1"

    if no_api:
        raise RuntimeError(
            "bbox cacheがありません。"
            f"NO_APIモードのためOpenAIを呼びません: {cache_path}"
        )

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    min_question_no, max_question_no = QUESTION_RANGES[category]

    client = OpenAI()

    prompt = f"""
薬剤師国家試験の問題ページ画像です。

このページ内に含まれる各問題について、図・表・化学構造式・グラフなど、
問題を解くために必要な画像領域を検出してください。

必ずJSONのみで返してください。

形式:
[
  {{
    "question_no": {min_question_no},
    "has_figure": true,
    "figure_bbox": [left, top, right, bottom]
  }}
]

ルール:
- bboxは画像左上を原点としたピクセル座標で返してください。
- figure_bboxは、図・表・構造式・グラフ・模式図など必要な視覚情報だけを囲んでください。
- 問題文や選択肢の文章は原則として含めないでください。
- ただし、選択肢そのものが図・構造式・表の場合は、その選択肢部分を含めてください。
- 図がない問題は has_figure:false とし、figure_bbox:null にしてください。
- 問番号が読めない場合は省略してください。
- 問{min_question_no}〜問{max_question_no}以外は無視してください。
"""

    response = client.responses.create(
        model=OPENAI_VISION_MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    },
                    {
                        "type": "input_image",
                        "image_url": image_to_data_url(image_path),
                    },
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    result = normalize_bbox_result(
        data=data,
        category=category,
    )

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"💾 bbox cache保存: {cache_path}")

    return result
