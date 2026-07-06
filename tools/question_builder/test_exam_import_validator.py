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

    target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

    exam_numbers = args.exam or [111, 110, 109]

    for exam_number in exam_numbers:
        validate_exam_import(
            target_file=target_file,
            exam_number=exam_number,
            expected_count=args.expected_count,
        )


if __name__ == "__main__":
    main()
