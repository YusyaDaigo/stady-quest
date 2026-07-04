from config import SOURCE_MATERIALS_DIR
from materials.material_loader import load_materials
from parsers.parser_factory import parse_material


def generate_questions(exam: str, category: str, count: int = 1):
    source_dir = SOURCE_MATERIALS_DIR / exam / category

    materials = load_materials(source_dir)

    raw_questions = []

    for material in materials:
        raw_questions.extend(parse_material(material))

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

def generate_questions(exam: str, category: str, count: int = 1):
    source_dir = SOURCE_MATERIALS_DIR / exam / category

    materials = load_materials(source_dir)

    raw_questions = []

    for material in materials:
        raw_questions.extend(
            parse_material(material)
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