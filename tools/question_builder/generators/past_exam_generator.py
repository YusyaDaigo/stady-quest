from config import SOURCE_MATERIALS_DIR
from materials.material_loader import load_materials


def parse_txt_question(text: str):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    question = lines[0]

    choices = []
    answer = None
    explanation = ""

    answer_map = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
    }

    for line in lines[1:]:
        if line.startswith("A."):
            choices.append(line.replace("A.", "", 1).strip())
        elif line.startswith("B."):
            choices.append(line.replace("B.", "", 1).strip())
        elif line.startswith("C."):
            choices.append(line.replace("C.", "", 1).strip())
        elif line.startswith("D."):
            choices.append(line.replace("D.", "", 1).strip())
        elif line.startswith("E."):
            choices.append(line.replace("E.", "", 1).strip())
        elif line.startswith("答え:"):
            answer_text = line.replace("答え:", "", 1).strip()
            answer = answer_map.get(answer_text)
        elif line.startswith("解説:"):
            explanation = line.replace("解説:", "", 1).strip()

    return {
        "question": question,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }


def material_to_raw_questions(material: dict):
    content = material["content"]

    if material["type"] == "json":
        if isinstance(content, list):
            return content
        return [content]

    if material["type"] == "txt":
        return [parse_txt_question(content)]

    raise ValueError(
        f"未対応の素材タイプです: {material['type']}"
    )


def generate_questions(exam: str, category: str, count: int = 1):
    source_dir = SOURCE_MATERIALS_DIR / exam / category

    materials = load_materials(source_dir)

    raw_questions = []

    for material in materials:
        raw_questions.extend(
            material_to_raw_questions(material)
        )

    questions = []

    for raw in raw_questions[:count]:
        questions.append(
            {
                "subject": exam,
                "category": category.upper(),
                "question": raw["question"],
                "choices": raw["choices"],
                "answer": raw["answer"],
                "explanation": raw["explanation"],
            }
        )

    return questions