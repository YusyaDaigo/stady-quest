import argparse
from pathlib import Path

from config import (
    BACKUP_DIR,
    EXAM_PATHS,
    QUESTION_FILES,
    INSERT_MARKER,
)

from formatters.js_formatter import build_question_block
from checkers.duplicate_checker import is_duplicate_question
from exporters.file_exporter import backup_file, insert_question_blocks
from validators.question_validator import validate_question
from generators.generator_factory import get_generator


def get_target_file(exam: str, category: str) -> Path:
    if exam not in EXAM_PATHS:
        raise ValueError(f"未対応の資格です: {exam}")

    if category not in QUESTION_FILES:
        raise ValueError(f"未対応のカテゴリです: {category}")

    return EXAM_PATHS[exam] / QUESTION_FILES[category]



def add_questions(target_file: Path, questions: list):
    text = target_file.read_text(encoding="utf-8")

    blocks = []

    for question in questions:
        
        validate_question(question)

        if is_duplicate_question(question, text):
            print(f"⚠️ 重複スキップ: {question['question']}")
            continue

        blocks.append(build_question_block(question))

    return insert_question_blocks(target_file, blocks)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--exam",
        required=True,
        help="資格名"
    )

    parser.add_argument(
        "--category",
        required=True,
        help="カテゴリ"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="生成数"
    )

    parser.add_argument(
        "--generator",
        default="static",
        help="使用するGenerator"
    )

    args = parser.parse_args()

    exam = args.exam
    category = args.category
    count = args.count

    target_file = get_target_file(exam, category)

    if not target_file.exists():
        raise FileNotFoundError(f"対象ファイルが存在しません: {target_file}")

    backup_path = backup_file(target_file)

    generator = get_generator(args.generator)

    questions = generator(
        exam=exam,
        category=category,
        count=count,
    )

    success = add_questions(target_file, questions)

    if success:
        print("✅ 問題追加完了")
        print(f"📄 対象: {target_file}")
        print(f"🛡️ バックアップ: {backup_path}")
    else:
        print("⏭️ 処理をスキップしました")


if __name__ == "__main__":
    main()