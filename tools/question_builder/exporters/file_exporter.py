import shutil
from datetime import datetime
from pathlib import Path

from config import BACKUP_DIR, INSERT_MARKER


def backup_file(target_file: Path):
    BACKUP_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"{target_file.name}.{timestamp}.bak"

    shutil.copy2(target_file, backup_path)

    return backup_path


def insert_question_blocks(target_file: Path, question_blocks: list):
    text = target_file.read_text(encoding="utf-8")

    if INSERT_MARKER not in text:
        raise ValueError(f"マーカーが見つかりません: {INSERT_MARKER}")

    if not question_blocks:
        print("⏭️ 追加する問題がありません")
        return False

    insert_text = "\n".join(question_blocks) + "\n  " + INSERT_MARKER
    updated_text = text.replace(INSERT_MARKER, insert_text, 1)

    target_file.write_text(updated_text, encoding="utf-8")

    return True