import json
from pathlib import Path


def load_materials(source_dir: Path):
    materials = []

    json_files = sorted(source_dir.glob("*.json"))

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        materials.append({
            "type": "json",
            "path": json_file,
            "content": data,
        })

    return materials