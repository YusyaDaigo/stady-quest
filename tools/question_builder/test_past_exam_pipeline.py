import argparse
from pathlib import Path

from pipelines.past_exam_pipeline import run_past_exam_pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int, required=True)
    parser.add_argument("--start-page", type=int, default=2)
    parser.add_argument("--max-pages", type=int, default=999)

    args = parser.parse_args()

    exam_number = args.exam

    question_pdf_path = Path(
        f"source_materials/pharmacy/required/pdf/{exam_number}_required.pdf"
    )
    answer_pdf_path = Path(
        f"source_materials/pharmacy/required/pdf/{exam_number}_answers.pdf"
    )

    if not question_pdf_path.exists():
        raise FileNotFoundError(f"問題PDFが見つかりません: {question_pdf_path}")

    if not answer_pdf_path.exists():
        raise FileNotFoundError(f"解答PDFが見つかりません: {answer_pdf_path}")

    run_past_exam_pipeline(
        exam="pharmacy",
        category="required",
        exam_number=exam_number,
        question_pdf_path=question_pdf_path,
        answer_pdf_path=answer_pdf_path,
        vision_engine_name="openai",
        answer_parser="vision",
        start_page=args.start_page,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    main()
