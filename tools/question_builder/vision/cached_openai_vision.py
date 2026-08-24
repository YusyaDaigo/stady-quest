import json
import os
from pathlib import Path

from vision.openai_vision import analyze_page as openai_analyze_page


def get_vision_cache_path(
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
        / "vision"
        / exam_number
    )

    if part_name is not None:
        cache_dir = cache_dir / part_name

    return cache_dir / f"{image_path.stem}.json"


def analyze_page(
    image_path: Path,
    category: str = "required",
):
    cache_path = get_vision_cache_path(
        image_path=image_path,
        category=category,
    )

    if cache_path.exists():
        print(f"📦 vision cache使用: {cache_path}")
        return json.loads(
            cache_path.read_text(encoding="utf-8")
        )

    no_api = os.getenv("STUDY_QUEST_NO_API") == "1"

    if no_api:
        raise RuntimeError(
            "vision cacheがありません。"
            f"NO_APIモードのためOpenAIを呼びません: {cache_path}"
        )

    result = openai_analyze_page(
        image_path,
        category=category,
    )

    cache_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    cache_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"💾 vision cache保存: {cache_path}")

    return result
