import math
from pathlib import Path

from PIL import Image, ImageChops


def trim_white_margin(image: Image.Image, padding: int = 24) -> Image.Image:
    """
    白背景の余白を自動で削る。
    PDF由来の白背景ページから、文字・図がある範囲だけを残す。
    """
    rgb_image = image.convert("RGB")
    background = Image.new("RGB", rgb_image.size, (255, 255, 255))

    diff = ImageChops.difference(rgb_image, background)
    bbox = diff.getbbox()

    if not bbox:
        return image

    left, top, right, bottom = bbox

    left = max(left - padding, 0)
    top = max(top - padding, 0)
    right = min(right + padding, image.width)
    bottom = min(bottom + padding, image.height)

    return image.crop((left, top, right, bottom))


def crop_page_by_question_index(
    page_image_path: Path,
    output_path: Path,
    question_index: int,
    question_count: int,
) -> Path:
    if question_index < 1 or question_index > question_count:
        raise ValueError(
            f"question_index は 1〜{question_count} の範囲で指定してください"
        )

    if question_count <= 0:
        raise ValueError("question_count は 1以上で指定してください")

    image = Image.open(page_image_path).convert("RGB")
    width, height = image.size

    part_height = height / question_count

    top = math.floor(part_height * (question_index - 1))
    bottom = math.ceil(part_height * question_index)

    # 境界ギリギリで図や選択肢が切れないよう、上下に余白を少し追加
    margin = math.floor(part_height * 0.18)

    top = max(0, top - margin)
    bottom = min(height, bottom + margin)

    cropped = image.crop((0, top, width, bottom))

    # 白余白を削る
    cropped = trim_white_margin(cropped, padding=36)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path)

    return output_path