import re


def extract_questions_from_js(text: str):
    pattern = re.compile(
        r'examNumber:\s*(\d+),.*?'
        r'sourceNumber:\s*(\d+),.*?'
        r'field:\s*"([^"]*)",.*?'
        r'question:\s*\n\s*"([^"]*)",.*?'
        r'choices:\s*\[(.*?)\].*?'
        r'answer:\s*(\d+),.*?'
        r'explanation:\s*\n\s*"([^"]*)"',
        re.DOTALL,
    )

    questions = []

    for match in pattern.finditer(text):
        choices_block = match.group(5)

        choices = re.findall(
            r'"([^"]*)"',
            choices_block
        )

        questions.append(
            {
                "examNumber": int(match.group(1)),
                "sourceNumber": int(match.group(2)),
                "field": match.group(3),
                "question": match.group(4),
                "choices": choices,
                "answer": int(match.group(6)),
                "explanation": match.group(7),
            }
        )

    return questions