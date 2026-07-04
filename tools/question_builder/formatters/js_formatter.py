def build_question_block(question_data: dict) -> str:
    choices_text = ",\n".join(
        [f'    "{choice}"' for choice in question_data["choices"]]
    )

    source_type = question_data.get("sourceType", "manual")
    exam_number = question_data.get("examNumber")
    source_number = question_data.get("sourceNumber")
    field = question_data.get("field", "")

    metadata_lines = f'''
    sourceType: "{source_type}",'''

    if exam_number is not None:
        metadata_lines += f'''
    examNumber: {exam_number},'''

    if source_number is not None:
        metadata_lines += f'''
    sourceNumber: {source_number},'''

    if field:
        metadata_lines += f'''
    field: "{field}",'''

    return f'''
  {{
    subject: "{question_data["subject"]}",
    category: CATEGORIES.{question_data["category"]},
{metadata_lines}

    question:
      "{question_data["question"]}",

    choices: [
{choices_text}
    ],

    answer: {question_data["answer"]},

    explanation:
      "{question_data["explanation"]}"
  }},
'''