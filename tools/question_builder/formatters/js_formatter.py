def escape_js_text(text: str) -> str:
    if text is None:
        return ""

    text = str(text)

    # 改行・タブ・余分な空白を1行にまとめる
    text = " ".join(text.split())

    # JavaScript文字列で壊れやすい文字をエスケープ
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')

    # OCRで混ざりやすい全角スラッシュを半角へ
    text = text.replace("／", "/")

    return text


def build_question_block(question_data: dict) -> str:
    escaped_question = escape_js_text(question_data["question"])
    escaped_explanation = escape_js_text(question_data.get("explanation", ""))

    escaped_choices = [
        escape_js_text(choice)
        for choice in question_data["choices"]
    ]

    choices_text = ",\n".join(
        [f'    "{choice}"' for choice in escaped_choices]
    )

    source_type = question_data.get("sourceType", "manual")
    exam_number = question_data.get("examNumber")
    source_number = question_data.get("sourceNumber")
    field = escape_js_text(question_data.get("field", ""))

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
      "{escaped_question}",

    choices: [
{choices_text}
    ],

    answer: {question_data["answer"]},

    explanation:
      "{escaped_explanation}"
  }},
'''