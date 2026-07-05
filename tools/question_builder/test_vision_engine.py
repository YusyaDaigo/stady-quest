from pathlib import Path

from vision.vision_factory import get_vision_engine


image_path = Path("source_materials/pharmacy/required/images/111/page_6.png")

vision_engine = get_vision_engine("openai")

questions = vision_engine(image_path)

print(f"抽出数: {len(questions)}")

for q in questions:
    print("-----")
    print("問", q["question_no"])
    print("図あり:", q.get("has_image"))
    print(q["question"])