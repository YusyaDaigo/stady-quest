from pathlib import Path

from vision.vision_factory import get_vision_engine


image_path = Path("source_materials/pharmacy/required/images/111_required/page_2.png")

vision_engine = get_vision_engine("openai")

questions = vision_engine(image_path)

print(f"抽出数: {len(questions)}")

for question in questions:
    print(question["question_no"], question["question"])