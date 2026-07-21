from __future__ import annotations

import json
from typing import Any, Iterable


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
) -> str:
    """
    Knowledgeを根拠とする問題生成プロンプトを作る。
    """

    if not knowledge_items:
        raise ValueError(
            "knowledge_items must not be empty"
        )

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

    return f"""
あなたは二等無人航空機操縦士試験の問題作成者です。

以下のKnowledgeだけを根拠として、
問題を{count}問作成してください。

Knowledgeに記載されていない情報を、
推測や一般知識で補ってはいけません。

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

【作問条件】
・下記Knowledgeだけを根拠とする
・選択肢は必ず3つ
・正答は必ず1つ
・answerは0始まり
・難易度は{difficulty}
・問題同士を重複させない
・単純な語句穴埋めだけにしない
・ケース問題は禁止
・知識問題のみとする
・曖昧な選択肢を作らない
・根拠のない数値、条件、制度を作らない
・正答だけでなく誤答の理由も説明する
・Knowledgeの文面を不自然に丸写ししない
・問題文にKnowledge IDを記載しない
・JSON以外の文章を出力しない

【各問題のJSON形式】
{{
  "question": "問題文",
  "choices": [
    "選択肢1",
    "選択肢2",
    "選択肢3"
  ],
  "answer": 0,
  "explanation": "正答の根拠と、他の選択肢が誤りである理由",
  "figureType": "none",
  "figureData": {{}}
}}

【出力形式】
上記形式のオブジェクトを{count}件含む、
JSON配列のみを出力してください。

【根拠Knowledge】
{knowledge_context}
""".strip()
