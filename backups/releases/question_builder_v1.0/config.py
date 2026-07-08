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

SOURCE_MATERIALS_DIR = BASE_DIR / "source_materials"

OPENAI_VISION_MODEL = "gpt-5.5"

PHARMACY_FIELD_ALIASES = {
    "物理": "物理",
    "化学": "化学",
    "生物": "生物",
    "衛生": "衛生",
    "薬理": "薬理",
    "薬剤": "薬剤",
    "病態": "病態・薬物治療",
    "病態・薬物治療": "病態・薬物治療",
    "法規": "法規・制度・倫理",
    "法規・制度・倫理": "法規・制度・倫理",
    "実務": "実務",
}