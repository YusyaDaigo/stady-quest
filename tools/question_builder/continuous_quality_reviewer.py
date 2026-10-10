from __future__ import annotations

import json
from typing import Any

from tools.question_builder.core.ai_client import (
    OpenAITextClient,
)


REQUIRED_REVIEW_FIELDS = {
    "decision",
    "factualAccuracy",
    "answerUniqueness",
    "grounding",
    "distractorQuality",
    "explanationQuality",
    "difficultyEstimate",
    "difficultyMatch",
    "issues",
    "revisionInstructions",
}


def validate_quality_review(
    review: dict[str, Any],
) -> None:
    if not isinstance(
        review,
        dict,
    ):
        raise ValueError(
            "quality review must be an object"
        )

    missing = (
        REQUIRED_REVIEW_FIELDS
        - review.keys()
    )

    if missing:
        raise ValueError(
            "quality review missing fields: "
            f"{sorted(missing)}"
        )

    if review["decision"] not in {
        "pass",
        "revise",
        "reject",
    }:
        raise ValueError(
            "invalid review decision"
        )

    for field in [
        "factualAccuracy",
        "answerUniqueness",
        "grounding",
        "distractorQuality",
        "explanationQuality",
    ]:
        if review[field] not in {
            "pass",
            "fail",
        }:
            raise ValueError(
                f"invalid {field}"
            )

    difficulty = review[
        "difficultyEstimate"
    ]

    if (
        not isinstance(
            difficulty,
            int,
        )
        or not 1 <= difficulty <= 5
    ):
        raise ValueError(
            "difficultyEstimate "
            "must be 1..5"
        )

    if not isinstance(
        review["difficultyMatch"],
        bool,
    ):
        raise ValueError(
            "difficultyMatch "
            "must be boolean"
        )

    for field in [
        "issues",
        "revisionInstructions",
    ]:
        value = review[field]

        if not isinstance(
            value,
            list,
        ):
            raise ValueError(
                f"{field} must be a list"
            )

        if not all(
            isinstance(item, str)
            and item.strip()
            for item in value
        ):
            raise ValueError(
                f"{field} must contain "
                "non-empty strings"
            )


def build_quality_review_prompt(
    *,
    knowledge: dict[str, Any],
    question: dict[str, Any],
    difficulty_min: int,
    difficulty_max: int,
    target_difficulty: int,
) -> str:
    knowledge_json = json.dumps(
        knowledge,
        ensure_ascii=False,
        indent=2,
    )

    question_json = json.dumps(
        question,
        ensure_ascii=False,
        indent=2,
    )

    return f"""
あなたはStudy QUESTの問題品質審査担当です。

以下のKnowledgeだけを根拠として、
生成された問題を厳格に審査してください。

外部知識で補完しないでください。
Knowledgeに書かれていない事実を
正しいものとして扱わないでください。

設定上の難易度範囲:
{difficulty_min}〜{difficulty_max}

今回の生成目標難易度:
{target_difficulty}

（1=非常に易しい、5=非常に難しい）

difficultyMatch=true にしてよいのは、
difficultyEstimate が
今回の生成目標難易度
{target_difficulty}
と完全に一致する場合だけです。

範囲内に入っているだけでは
difficultyMatch=true にしてはいけません。

特に次を確認してください。

1. 正答はKnowledgeから直接確認できるか
2. 正答が一意か
3. 問題文に曖昧さがないか
4. 誤答選択肢が不自然な単語入れ替えだけに
   なっていないか
5. 消去法だけで簡単に解けすぎないか
6. 解説が正答の理由を明確に説明しているか
7. Knowledge外の専門用語・事実を
   持ち込んでいないか
8. 実際の難易度が目標範囲内か

難易度判定では、
単純な用語暗記や、
名称と番号の直接対応だけを問う問題は
低く評価してください。

decision:
- pass:
  そのまま採用候補にできる
- revise:
  根拠自体は使えるが問題を作り直すべき
- reject:
  Knowledge不足などで、
  この条件では良問にするのが困難

passにしてよいのは、
以下がすべてpassで、
difficultyMatch=trueの場合だけです。

factualAccuracy
answerUniqueness
grounding
distractorQuality
explanationQuality

JSONのみを返してください。

形式:

{{
  "decision": "pass|revise|reject",
  "factualAccuracy": "pass|fail",
  "answerUniqueness": "pass|fail",
  "grounding": "pass|fail",
  "distractorQuality": "pass|fail",
  "explanationQuality": "pass|fail",
  "difficultyEstimate": 1,
  "difficultyMatch": false,
  "issues": [
    "問題点"
  ],
  "revisionInstructions": [
    "修正指示"
  ]
}}

Knowledge:
{knowledge_json}

生成問題:
{question_json}
""".strip()


def parse_quality_review_response(
    response_text: str,
) -> dict[str, Any]:
    text = str(
        response_text
    ).strip()

    if text.startswith(
        "```"
    ):
        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if (
            lines
            and lines[-1].strip()
            == "```"
        ):
            lines = lines[:-1]

        text = "\n".join(
            lines
        ).strip()

    review = json.loads(
        text
    )

    validate_quality_review(
        review
    )

    return review


class ContinuousQualityReviewer:
    def __init__(
        self,
        *,
        model: str = "gpt-5.5",
        max_api_calls: int = 1,
    ) -> None:
        self.ai_client = (
            OpenAITextClient(
                model=model,
                max_calls_per_process=(
                    max_api_calls
                ),
            )
        )

    def review(
        self,
        *,
        knowledge: dict[str, Any],
        question: dict[str, Any],
        difficulty_min: int,
        difficulty_max: int,
        target_difficulty: int,
        allow_api: bool = False,
    ) -> dict[str, Any]:
        prompt = (
            build_quality_review_prompt(
                knowledge=knowledge,
                question=question,
                difficulty_min=(
                    difficulty_min
                ),
                difficulty_max=(
                    difficulty_max
                ),
                target_difficulty=(
                    target_difficulty
                ),
            )
        )

        response = (
            self.ai_client.generate(
                prompt=prompt,
                allow_api=allow_api,
            )
        )

        return (
            parse_quality_review_response(
                response
            )
        )
