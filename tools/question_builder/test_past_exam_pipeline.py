from pathlib import Path

from pipelines.past_exam_pipeline import run_past_exam_pipeline


run_past_exam_pipeline(
    exam="pharmacy",
    category="required",
    exam_number=111,
    question_pdf_path=Path("source_materials/pharmacy/required/pdf/111_required.pdf"),
    answer_pdf_path=Path("source_materials/pharmacy/required/pdf/111_answers.pdf"),
    vision_engine_name="openai",
    start_page=6,
    max_pages=1,
)