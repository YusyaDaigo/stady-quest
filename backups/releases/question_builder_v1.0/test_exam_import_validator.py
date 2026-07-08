import argparse

from config import EXAM_PATHS, QUESTION_FILES
from validators.exam_import_validator import validate_exam_import


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int, action="append")
    parser.add_argument("--expected-count", type=int, default=90)

    args = parser.parse_args()

    exam = "pharmacy"
    category = "required"

    exam_numbers = args.exam or [111, 110, 109, 108, 107, 106]

    for exam_number in exam_numbers:
        yearly_file = EXAM_PATHS[exam] / f"required_{exam_number}.js"

        if yearly_file.exists():
            target_file = yearly_file
        else:
            target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

        validate_exam_import(
            target_file=target_file,
            exam_number=exam_number,
            expected_count=args.expected_count,
        )


if __name__ == "__main__":
    main()
