from pathlib import Path

from vision.vision_factory import get_vision_engine


image_path = Path("source_materials/pharmacy/required/images/111_required/page_2.png")

vision_engine = get_vision_engine("mock")

result = vision_engine(image_path)

print(result)