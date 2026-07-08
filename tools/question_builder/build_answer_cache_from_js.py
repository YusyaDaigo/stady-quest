import argparse
import json
from pathlib import Path

from explanations.explanation_reader import extract_questions_from_js


CACHE_DIR = Path(
    "tools/question_builder/cache/pharmacy/required/answers"
)

QUESTION_DIR = Path(
    "src/exams/pharmacy/questions"
)


def build_answer_cache(exam_number: int):
    source_file = QUESTION_DIR / f"required_{exam_number}.js"

    if not source_file.exists():
        raise FileNotFoundError(source_file)

    text = source_file.read_text(encoding="utf-8")
    questions = extract_questions_from_js(text)

    answers = {}

    for question in questions:
        if question.get("examNumber") != exam_number:
            continue

        source_number = question.get("sourceNumber")
        answer = question.get("answer")

        if source_number is None or answer is None:
            continue

        answers[int(source_number)] = {
            "field": question.get("field", ""),
            "answer": int(answer),
        }

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    output_path = CACHE_DIR / f"{exam_number}.json"
    output_path.write_text(
        json.dumps(answers, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"✅ answer cache作成: {output_path}")
    print(f"問題数: {len(answers)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int)
    parser.add_argument("--all", action="store_true")

    args = parser.parse_args()

    if args.all:
        for exam_number in range(97, 112):
            build_answer_cache(exam_number)
        return

    if args.exam is None:
        raise SystemExit("--exam または --all を指定してください")

    build_answer_cache(args.exam)


if __name__ == "__main__":
    main()
