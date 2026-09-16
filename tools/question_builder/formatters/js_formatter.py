def escape_js_text(text: str) -> str:
    if text is None:
        return ""

    text = str(text)

    # 改行コードを統一
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # 各行内のタブ・連続空白を整理しつつ、
    # 問題文の段落改行は保持する
    lines = []

    for line in text.split("\n"):
        normalized_line = " ".join(
            line.split()
        )
        lines.append(normalized_line)

    text = "\n".join(lines)

    # 3行以上の連続改行は2行へまとめる
    while "\n\n\n" in text:
        text = text.replace(
            "\n\n\n",
            "\n\n",
        )

    # JavaScript文字列内で改行を保持する
    text = text.replace("\\", "\\\\")
    text = text.replace("\n", "\\n")
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
    required_selections = question_data.get(
        "requiredSelections"
    )
    scoring_status = question_data.get(
        "scoringStatus"
    )
    has_image = question_data.get("hasImage", False)
    image = escape_js_text(question_data.get("image", ""))

    case_id = question_data.get("caseId")
    case_context = escape_js_text(
        question_data.get("caseContext", "")
    )

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
        
    if has_image:
        metadata_lines += f'''
    hasImage: true,'''

    if image:
        metadata_lines += f'''
    image: "{image}",'''

    if case_id is not None:
        metadata_lines += f'''
    caseId: "{case_id}",'''

    if case_context:
        metadata_lines += f'''
    caseContext:
      "{case_context}",'''

    if scoring_status is not None:
        metadata_lines += f'''
    scoringStatus: "{scoring_status}",'''

    required_selections_line = ""

    if required_selections is not None:
        required_selections_line = f'''
    requiredSelections: {required_selections},'''

    answer_value = (
        "null"
        if question_data["answer"] is None
        else str(question_data["answer"])
    )

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

    answer: {answer_value},
{required_selections_line}

    explanation:
      "{escaped_explanation}"
  }},
'''
