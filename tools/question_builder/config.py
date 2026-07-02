from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
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

QUESTION_JSON_PATH = BASE_DIR / "tools/question_builder/generated_questions.json"

INSERT_MARKER = "// AI_QUESTION_INSERT_HERE"