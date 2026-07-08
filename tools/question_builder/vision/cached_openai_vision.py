import json
import os
from pathlib import Path

from vision.openai_vision import analyze_page as openai_analyze_page


VISION_CACHE_DIR = Path(
    "tools/question_builder/cache/pharmacy/required/vision"
)


def get_vision_cache_path(image_path: Path) -> Path:
    parts = image_path.parts

    try:
        exam_number = parts[parts.index("images") + 1]
    except Exception:
        exam_number = "unknown"

    return VISION_CACHE_DIR / exam_number / f"{image_path.stem}.json"


def analyze_page(image_path: Path):
    cache_path = get_vision_cache_path(image_path)

    if cache_path.exists():
        print(f"📦 vision cache使用: {cache_path}")
        return json.loads(
            cache_path.read_text(encoding="utf-8")
        )

    no_api = os.getenv("STUDY_QUEST_NO_API") == "1"

    if no_api:
        raise RuntimeError(
            f"vision cacheがありません。NO_APIモードのためOpenAIを呼びません: {cache_path}"
        )

    result = openai_analyze_page(image_path)

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"💾 vision cache保存: {cache_path}")

    return result
