from config import EXAM_PATHS, QUESTION_FILES
from validators.exam_import_validator import validate_exam_import


exam = "pharmacy"
category = "required"

target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

for exam_number in [111, 110, 109]:
    validate_exam_import(
        target_file=target_file,
        exam_number=exam_number,
        expected_count=90,
    )