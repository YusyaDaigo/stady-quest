from __future__ import annotations

import json
from typing import Any, Iterable

from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)


def _normalize_keywords(
    keywords: Iterable[str] | None,
) -> list[str]:
    results: list[str] = []
    seen: set[str] = set()

    for raw_keyword in keywords or []:
        keyword = str(raw_keyword).strip()

        if not keyword or keyword in seen:
            continue

        seen.add(keyword)
        results.append(keyword)

    return results


def _build_knowledge_context(
    knowledge_items: list[dict[str, Any]],
) -> str:
    """
    Retrieverが返したKnowledgeを、
    AIへ渡す根拠資料として整形する。
    """

    blocks: list[str] = []

    for index, item in enumerate(
        knowledge_items,
        start=1,
    ):
        knowledge_id = str(
            item.get("id", "")
        ).strip()

        title = str(
            item.get("title", "")
        ).strip()

        pages = item.get("pages", [])
        text = str(
            item.get("text", "")
        ).strip()

        block = "\n".join(
            [
                f"【Knowledge {index}】",
                f"id: {knowledge_id}",
                f"title: {title}",
                (
                    "pages: "
                    + json.dumps(
                        pages,
                        ensure_ascii=False,
                    )
                ),
                "text:",
                text,
            ]
        )

        blocks.append(block)

    return "\n\n".join(blocks)


def build_rag_question_generation_prompt(
    *,
    section: str,
    section_display_name: str,
    difficulty: int,
    count: int,
    keywords: Iterable[str] | None,
    knowledge_items: list[dict[str, Any]],
    exam: str = "drone",
    question_type: str | None = None,
) -> str:
    """
    Knowledgeを根拠とする問題生成プロンプトを作る。

    examを省略した場合は既存互換のためdroneを使用する。
    """

    if not knowledge_items:
        raise ValueError(
            "knowledge_items must not be empty"
        )

    profile = get_exam_generation_profile(
        exam
    )

    normalized_question_type = None

    if question_type is not None:
        normalized_question_type = (
            str(question_type)
            .strip()
            .lower()
        )

    question_types = profile.get(
        "questionTypes"
    )

    if question_types:
        if not normalized_question_type:
            raise ValueError(
                "question_type is required for "
                f"{exam}"
            )

        if (
            normalized_question_type
            not in question_types
        ):
            raise ValueError(
                "Unsupported question_type for "
                f"{exam}: "
                f"{question_type}. "
                "Supported types: "
                f"{sorted(question_types)}"
            )

        choice_count = question_types[
            normalized_question_type
        ]["choiceCount"]

    else:
        if normalized_question_type:
            raise ValueError(
                "question_type is not supported "
                f"for {exam}"
            )

        choice_count = profile[
            "choiceCount"
        ]

    normalized_keywords = _normalize_keywords(
        keywords
    )

    keyword_text = (
        "、".join(normalized_keywords)
        if normalized_keywords
        else "指定なし"
    )

    knowledge_context = (
        _build_knowledge_context(
            knowledge_items
        )
    )

    generation_rules = "\n".join(
        f"・{rule}"
        for rule in profile[
            "generationRules"
        ]
    )

    if (
        normalized_question_type
        == "true_false"
    ):
        choice_examples = [
            "正しい",
            "誤り",
        ]
    else:
        choice_examples = [
            f"選択肢{index}"
            for index in range(
                1,
                choice_count + 1,
            )
        ]

    choices_json = ",\n".join(
        f'    "{choice}"'
        for choice in choice_examples
    )

    question_type_rule = ""

    question_type_json = ""

    if normalized_question_type:
        question_type_rule = (
            "・questionTypeは"
            f'"{normalized_question_type}"'
            "とする"
        )

        question_type_json = (
            '  "questionType": '
            f'"{normalized_question_type}",\n'
        )

    supported_figure_types = ", ".join(
        profile["supportedFigureTypes"]
    )

    answer_index_base = profile[
        "answerIndexBase"
    ]

    return f"""
あなたは{profile["displayName"]}の問題作成者です。

以下のKnowledgeだけを根拠として、
問題を{count}問作成してください。

Knowledgeに記載されていない情報を、
推測や一般知識で補ってはいけません。

【対象資格】
exam: {exam}
資格名: {profile["displayName"]}

【対象分野】
section: {section}
分野名: {section_display_name}
検索キーワード: {keyword_text}
難易度: {difficulty}

【難易度の目安】
1: 基本用語や明確な規則を確認する
2: 基本知識の違いを区別する
3: 複数の関連知識を整理して判断する
4: 類似制度や条件の細かな違いを判断する
5: 複数条件を正確に比較して判断する

【資格別生成ルール】
{generation_rules}

【今回の作問条件】
・下記Knowledgeだけを根拠とする
・選択肢は必ず{choice_count}つ
・正答は必ず1つ
・answerは{answer_index_base}始まり
・難易度は{difficulty}
・問題同士を重複させない
・曖昧な選択肢を作らない
・根拠のない数値、条件、制度を作らない
・正答の根拠を説明する
・Knowledgeの文面を不自然に丸写ししない
・問題文にKnowledge IDを記載しない
・figureTypeは次から選択する: {supported_figure_types}
{question_type_rule}
・JSON以外の文章を出力しない

【各問題のJSON形式】
{{
{question_type_json}  "question": "問題文",
  "choices": [
{choices_json}
  ],
  "answer": {answer_index_base},
  "explanation": "正答の根拠と必要な解説",
  "figureType": "none",
  "figureData": {{}}
}}

【出力形式】
上記形式のオブジェクトを{count}件含む、
JSON配列のみを出力してください。

【根拠Knowledge】
{knowledge_context}
""".strip()
