import math
from pathlib import Path

from PIL import Image


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

    image = Image.open(page_image_path)
    width, height = image.size

    part_height = height / question_count

    top = math.floor(part_height * (question_index - 1))
    bottom = math.ceil(part_height * question_index)

    cropped = image.crop((0, top, width, bottom))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path)

    return output_path