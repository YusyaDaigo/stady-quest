from pathlib import Path

from PIL import Image


def crop_by_bbox(
    page_image_path: Path,
    output_path: Path,
    bbox,
    padding: int = 36,
) -> Path:
    image = Image.open(page_image_path).convert("RGB")
    width, height = image.size

    left, top, right, bottom = bbox

    left = max(0, int(left) - padding)
    top = max(0, int(top) - padding)
    right = min(width, int(right) + padding)
    bottom = min(height, int(bottom) + padding)

    if right <= left or bottom <= top:
        raise ValueError(f"不正なbboxです: {bbox}")

    cropped = image.crop((left, top, right, bottom))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path)

    return output_path
