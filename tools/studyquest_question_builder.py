import json
import shutil
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
BACKUP_DIR = BASE_DIR / "backups"

EXAM_PATHS = {
    "drone": BASE_DIR / "src/exams/drone/questions",
    "pharmacy": BASE_DIR / "src/exams/pharmacy/questions",
}

QUESTION_FILES = {
    "required": "required.js",
    "theory": "theory.js",
    "practical": "practical.js",
}


def backup_file(target_file: Path):
    BACKUP_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"{target_file.name}.{timestamp}.bak"

    shutil.copy2(target_file, backup_path)

    return backup_path


def get_target_file(exam: str, category: str) -> Path:
    if exam not in EXAM_PATHS:
        raise ValueError(f"未対応の資格です: {exam}")

    if category not in QUESTION_FILES:
        raise ValueError(f"未対応のカテゴリです: {category}")

    return EXAM_PATHS[exam] / QUESTION_FILES[category]


def load_questions_from_json(json_path: Path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_question_block(question_data: dict) -> str:
    choices_text = ",\n".join(
        [f'    "{choice}"' for choice in question_data["choices"]]
    )

    return f'''
  {{
    subject: "{question_data["subject"]}",
    category: CATEGORIES.{question_data["category"]},

    question:
      "{question_data["question"]}",

    choices: [
{choices_text}
    ],

    answer: {question_data["answer"]},

    explanation:
      "{question_data["explanation"]}"
  }},
'''


def add_questions(target_file: Path, questions: list):
    text = target_file.read_text(encoding="utf-8")

    marker = "// AI_QUESTION_INSERT_HERE"

    if marker not in text:
        raise ValueError(f"マーカーが見つかりません: {marker}")

    blocks = []

    for question in questions:
        if question["question"] in text:
            print(f"⚠️ 重複スキップ: {question['question']}")
            continue

        blocks.append(build_question_block(question))

    if not blocks:
        print("⏭️ 追加する問題がありません")
        return False

    insert_text = "\n".join(blocks) + "\n  " + marker

    updated_text = text.replace(marker, insert_text, 1)

    target_file.write_text(updated_text, encoding="utf-8")

    return True


def main():
    exam = "pharmacy"
    category = "required"
    json_path = BASE_DIR / "tools/generated_questions.json"

    target_file = get_target_file(exam, category)

    if not target_file.exists():
        raise FileNotFoundError(f"対象ファイルが存在しません: {target_file}")

    questions = load_questions_from_json(json_path)

    backup_path = backup_file(target_file)

    success = add_questions(target_file, questions)

    if success:
        print("✅ 問題追加完了")
        print(f"📄 対象: {target_file}")
        print(f"🛡️ バックアップ: {backup_path}")
    else:
        print("⏭️ 処理をスキップしました")


if __name__ == "__main__":
    main()