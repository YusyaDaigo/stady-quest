def build_question_block(question_data: dict) -> str:
    choices_text = ",\n".join(
        [f'    "{choice}"' for choice in question_data["choices"]]
    )

    return f'''
  {{
    subject: "{question_data["subject"]}",
    category: CATEGORIES.{question_data["category"]},

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