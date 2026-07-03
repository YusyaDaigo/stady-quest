from generators.static_generator import generate_questions as static_generate_questions
from generators.past_exam_generator import generate_questions as past_exam_generate_questions


def get_generator(generator_name: str):
    if generator_name == "static":
        return static_generate_questions

    if generator_name == "past_exam":
        return past_exam_generate_questions

    raise ValueError(
        f"未対応のGeneratorです: {generator_name}"
    )