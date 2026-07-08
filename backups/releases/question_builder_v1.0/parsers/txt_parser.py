def parse_txt_question(text: str):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        raise ValueError("TXT素材が空です")

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

    return [
        {
            "question": question,
            "choices": choices,
            "answer": answer,
            "explanation": explanation,
        }
    ]