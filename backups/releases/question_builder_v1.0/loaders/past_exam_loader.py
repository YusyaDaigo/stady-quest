import json
from pathlib import Path


def load_past_exam_questions(source_dir: Path):
    questions = []

    json_files = sorted(source_dir.glob("*.json"))

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            questions.extend(data)
        else:
            questions.append(data)

    return questions