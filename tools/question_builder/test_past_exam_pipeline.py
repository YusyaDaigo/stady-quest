from pathlib import Path

from pipelines.past_exam_pipeline import run_past_exam_pipeline


run_past_exam_pipeline(
    exam="pharmacy",
    category="required",
    exam_number=109,
    question_pdf_path=Path("source_materials/pharmacy/required/pdf/109_required.pdf"),
    answer_pdf_path=Path("source_materials/pharmacy/required/pdf/109_answers.pdf"),
    vision_engine_name="openai",
    answer_parser="vision",
    start_page=39,
    max_pages=1,
)