from parsers.json_parser import parse_json_material
from parsers.txt_parser import parse_txt_question


def parse_material(material: dict):
    material_type = material["type"]
    content = material["content"]

    if material_type == "json":
        return parse_json_material(content)

    if material_type == "txt":
        return parse_txt_question(content)

    raise ValueError(
        f"未対応の素材タイプです: {material_type}"
    )