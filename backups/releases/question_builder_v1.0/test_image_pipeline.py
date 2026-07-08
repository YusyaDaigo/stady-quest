from pathlib import Path

from config import EXAM_PATHS, QUESTION_FILES
from images.image_pipeline import run_image_pipeline


exam = "pharmacy"
category = "required"
exam_number = 111

target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

run_image_pipeline(
    target_file=target_file,
    question_pdf_path=Path("source_materials/pharmacy/required/pdf/111_required.pdf"),
    exam=exam,
    category=category,
    exam_number=exam_number,
    start_number=21,
    end_number=90,
)