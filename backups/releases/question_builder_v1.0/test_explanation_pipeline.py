from config import EXAM_PATHS, QUESTION_FILES
from explanations.explanation_pipeline import run_explanation_pipeline


exam = "pharmacy"
category = "required"

target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

run_explanation_pipeline(
    target_file=target_file,
    exam_number=111,
    start_number=61,
    end_number=90,
)