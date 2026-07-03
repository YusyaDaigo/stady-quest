from config import SOURCE_MATERIALS_DIR
from materials.material_loader import load_materials


def generate_questions(exam: str, category: str, count: int = 1):
    source_dir = SOURCE_MATERIALS_DIR / exam / category

    materials = load_materials(source_dir)

    raw_questions = []

    for material in materials:
        content = material["content"]

        if isinstance(content, list):
            raw_questions.extend(content)
        else:
            raw_questions.append(content)

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