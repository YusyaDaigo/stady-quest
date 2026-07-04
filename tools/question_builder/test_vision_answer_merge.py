from pathlib import Path

from parsers.answer_pdf_parser import parse_required_answers_from_pdf
from vision.vision_factory import get_vision_engine
from generators.vision_question_builder import build_question_from_vision_result


exam = "pharmacy"
category = "required"

image_path = Path("source_materials/pharmacy/required/images/111_required/page_2.png")
answer_pdf_path = Path("source_materials/pharmacy/required/pdf/111_answers.pdf")

vision_engine = get_vision_engine("mock")
vision_result = vision_engine(image_path)

answer_data = parse_required_answers_from_pdf(answer_pdf_path)

question = build_question_from_vision_result(
    vision_result=vision_result,
    answer_data=answer_data,
    exam=exam,
    category=category,
)

print(question)