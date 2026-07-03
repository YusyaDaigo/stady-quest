import json
from pathlib import Path


def load_json_materials(source_dir: Path):
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


def load_txt_materials(source_dir: Path):
    materials = []

    txt_files = sorted(source_dir.glob("*.txt"))

    for txt_file in txt_files:
        text = txt_file.read_text(encoding="utf-8")

        materials.append({
            "type": "txt",
            "path": txt_file,
            "content": text,
        })

    return materials


def load_materials(source_dir: Path):
    materials = []

    materials.extend(load_json_materials(source_dir))
    materials.extend(load_txt_materials(source_dir))

    return materials