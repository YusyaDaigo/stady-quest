from parsers.json_parser import parse_json_material
from parsers.txt_parser import parse_txt_question
from parsers.pdf_parser import parse_pdf_material


def parse_material(material: dict):
    material_type = material["type"]
    content = material["content"]

    if material_type == "json":
        return parse_json_material(content)

    if material_type == "txt":
        return parse_txt_question(content)

    if material_type == "pdf":
        return parse_pdf_material(content)

    raise ValueError(
        f"未対応の素材タイプです: {material_type}"
    )