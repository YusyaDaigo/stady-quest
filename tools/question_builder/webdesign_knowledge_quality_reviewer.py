from __future__ import annotations

import json
from typing import Any

from tools.question_builder.core.ai_client import (
    OpenAITextClient,
)


REQUIRED_REVIEW_FIELDS = {
    "decision",
    "topicAlignment",
    "answerSupport",
    "factScope",
    "sectionConsistency",
    "candidateCoverage",
    "factAssessments",
    "issues",
    "recommendedFactIndexes",
}


def validate_knowledge_quality_review(
    review: dict[str, Any],
    *,
    fact_count: int,
    candidate_count: int,
) -> None:
    if not isinstance(
        review,
        dict,
    ):
        raise ValueError(
            "knowledge quality review must be an object"
        )

    missing = (
        REQUIRED_REVIEW_FIELDS
        - review.keys()
    )

    if missing:
        raise ValueError(
            "knowledge quality review missing fields: "
            f"{sorted(missing)}"
        )

    if review["decision"] not in {
        "pass",
        "hold",
        "reject",
    }:
        raise ValueError(
            "invalid knowledge QA decision"
        )

    for field in [
        "topicAlignment",
        "answerSupport",
        "factScope",
        "sectionConsistency",
    ]:
        if review[field] not in {
            "pass",
            "fail",
        }:
            raise ValueError(
                f"invalid {field}"
            )

    candidate_coverage = review[
        "candidateCoverage"
    ]

    if not isinstance(
        candidate_coverage,
        list,
    ):
        raise ValueError(
            "candidateCoverage must be a list"
        )

    if len(
        candidate_coverage
    ) != candidate_count:
        raise ValueError(
            "candidateCoverage length must "
            "match candidate fact count"
        )

    seen_candidate_indexes = set()

    for item in candidate_coverage:
        if not isinstance(
            item,
            dict,
        ):
            raise ValueError(
                "candidateCoverage items "
                "must be objects"
            )

        if set(item) != {
            "candidateIndex",
            "status",
        }:
            raise ValueError(
                "candidateCoverage item "
                "has invalid fields"
            )

        candidate_index = item[
            "candidateIndex"
        ]

        if (
            not isinstance(
                candidate_index,
                int,
            )
            or isinstance(
                candidate_index,
                bool,
            )
            or not (
                0
                <= candidate_index
                < candidate_count
            )
        ):
            raise ValueError(
                "invalid candidateIndex"
            )

        if (
            candidate_index
            in seen_candidate_indexes
        ):
            raise ValueError(
                "duplicate candidateIndex"
            )

        seen_candidate_indexes.add(
            candidate_index
        )

        if item["status"] not in {
            "supported",
            "unsupported",
        }:
            raise ValueError(
                "invalid candidateCoverage status"
            )

    fact_assessments = review[
        "factAssessments"
    ]

    if not isinstance(
        fact_assessments,
        list,
    ):
        raise ValueError(
            "factAssessments must be a list"
        )

    if len(
        fact_assessments
    ) != fact_count:
        raise ValueError(
            "factAssessments length must "
            "match fact count"
        )

    seen_fact_indexes = set()

    for item in fact_assessments:
        if not isinstance(
            item,
            dict,
        ):
            raise ValueError(
                "factAssessments items "
                "must be objects"
            )

        if set(item) != {
            "factIndex",
            "relevance",
        }:
            raise ValueError(
                "factAssessment has "
                "invalid fields"
            )

        fact_index = item[
            "factIndex"
        ]

        if (
            not isinstance(
                fact_index,
                int,
            )
            or isinstance(
                fact_index,
                bool,
            )
            or not (
                0 <= fact_index < fact_count
            )
        ):
            raise ValueError(
                "invalid factIndex"
            )

        if fact_index in seen_fact_indexes:
            raise ValueError(
                "duplicate factIndex"
            )

        seen_fact_indexes.add(
            fact_index
        )

        if item["relevance"] not in {
            "direct",
            "background",
            "out_of_scope",
        }:
            raise ValueError(
                "invalid fact relevance"
            )

    issues = review["issues"]

    if (
        not isinstance(
            issues,
            list,
        )
        or not all(
            isinstance(item, str)
            and item.strip()
            for item in issues
        )
    ):
        raise ValueError(
            "issues must be a list of "
            "non-empty strings"
        )

    indexes = review[
        "recommendedFactIndexes"
    ]

    if not isinstance(
        indexes,
        list,
    ):
        raise ValueError(
            "recommendedFactIndexes "
            "must be a list"
        )

    if any(
        not isinstance(index, int)
        or isinstance(index, bool)
        or not (
            0 <= index < fact_count
        )
        for index in indexes
    ):
        raise ValueError(
            "recommendedFactIndexes "
            "contains invalid index"
        )

    if (
        len(indexes)
        != len(set(indexes))
    ):
        raise ValueError(
            "recommendedFactIndexes "
            "contains duplicates"
        )

    direct_indexes = sorted(
        item["factIndex"]
        for item in fact_assessments
        if item["relevance"] == "direct"
    )

    if indexes != direct_indexes:
        raise ValueError(
            "recommendedFactIndexes must "
            "exactly match direct facts"
        )

    if (
        review["decision"] == "pass"
        and any(
            review[field] != "pass"
            for field in [
                "topicAlignment",
                "answerSupport",
                "factScope",
                "sectionConsistency",
            ]
        )
    ):
        raise ValueError(
            "pass requires all QA fields "
            "to pass"
        )

    if (
        review["decision"] == "pass"
        and len(indexes) != fact_count
    ):
        raise ValueError(
            "pass requires all verified facts "
            "to be directly usable"
        )

    if review["decision"] == "pass":
        if any(
            item["status"]
            != "supported"
            for item in candidate_coverage
        ):
            raise ValueError(
                "pass requires all candidate "
                "facts to be supported"
            )

        if any(
            item["relevance"]
            != "direct"
            for item in fact_assessments
        ):
            raise ValueError(
                "pass requires every verified "
                "fact to be direct"
            )


def build_knowledge_quality_prompt(
    *,
    knowledge: dict[str, Any],
) -> str:
    payload = {
        "id": knowledge.get("id"),
        "section": knowledge.get("section"),
        "title": knowledge.get("title"),
        "candidateFacts": knowledge.get(
            "candidateFacts",
            [],
        ),
        "verifiedFacts": knowledge.get(
            "facts",
            [],
        ),
        "answerExplanationSummary": (
            knowledge.get(
                "answerExplanationSummary"
            )
        ),
        "answerSection": knowledge.get(
            "answerSection"
        ),
        "sectionMatch": knowledge.get(
            "sectionMatch"
        ),
        "sourceQuestionNumbers": (
            knowledge.get(
                "sourceQuestionNumbers",
                [],
            )
        ),
    }

    knowledge_json = json.dumps(
        payload,
        ensure_ascii=False,
        indent=2,
    )

    return f"""
あなたはStudy QUESTの
WebDesign Knowledge品質審査担当です。

目的:
問題画像から抽出した論点と、
解答・解説画像から抽出した事実が、
同じ学習論点を適切に支えているかを
厳格に判定してください。

重要:
- 与えられたJSONだけを根拠にしてください。
- 外部知識を使って内容を訂正しないでください。
- 一般知識から不足情報を補わないでください。
- verifiedFactsが事実として正しいかを
  外部知識で判定する仕事ではありません。
- candidateFactsとverifiedFactsの
  論点整合性を判定してください。

判定項目:

topicAlignment:
candidateFactsの中心論点と
verifiedFactsの中心論点が一致するか。

answerSupport:
verifiedFactsに、
candidateFactsの論点を支える
十分な根拠が含まれるか。

factScope:
verifiedFactsの各項目が、
元問題を判断するための根拠として
直接必要な範囲に収まっているか。

単に同じ分野・同じテーマに属するだけでは
directと判定しないでください。

candidateCoverage:
candidateFactsを0始まりindexごとに確認し、
verifiedFactsによって直接支えられるなら
supported、
直接支えられないならunsupportedとしてください。

factAssessments:
verifiedFactsを0始まりindexごとに
必ず全件評価してください。

relevance:
- direct:
  元問題の中心論点や正答判断を
  直接支える事実
- background:
  内容上は関連するが、
  元問題の判断には直接必要でない
  周辺知識や一般説明
- out_of_scope:
  元問題の論点から外れる事実

重要:
同じ技術分野に属するという理由だけで
directにしてはいけません。

sectionConsistency:
section、answerSection、
sectionMatchに矛盾がないか。

recommendedFactIndexes:
factAssessmentsでdirectと判定した
verifiedFactsだけの0始まりindexを
昇順で指定してください。

decision:

pass:
- 4項目すべてpass
- candidateFactsがすべてsupported
- verifiedFactsがすべてdirect
- そのまま人間レビュー候補にできる

hold:
- 使用可能なdirect根拠は存在するが、
  backgroundやout_of_scopeの混入、
  candidateFactの未充足、
  論点ずれ、根拠不足などがあり
  人間確認が必要

reject:
- candidateFactsとverifiedFactsが
  実質的に対応していない、
  またはKnowledge根拠として
  使用困難

passでもreviewStatusを
approvedに変更してはいけません。
この判定は人間承認の前段階です。

JSONのみを返してください。

形式:
{{
  "decision": "pass|hold|reject",
  "topicAlignment": "pass|fail",
  "answerSupport": "pass|fail",
  "factScope": "pass|fail",
  "sectionConsistency": "pass|fail",
  "candidateCoverage": [
    {{
      "candidateIndex": 0,
      "status": "supported|unsupported"
    }}
  ],
  "factAssessments": [
    {{
      "factIndex": 0,
      "relevance": "direct|background|out_of_scope"
    }}
  ],
  "issues": [
    "問題点"
  ],
  "recommendedFactIndexes": [
    0,
    1
  ]
}}

Knowledge:
{knowledge_json}
""".strip()


def parse_knowledge_quality_response(
    response_text: str,
    *,
    fact_count: int,
    candidate_count: int,
) -> dict[str, Any]:
    text = str(
        response_text
    ).strip()

    if text.startswith("```"):
        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if (
            lines
            and lines[-1].strip() == "```"
        ):
            lines = lines[:-1]

        text = "\n".join(
            lines
        ).strip()

    review = json.loads(
        text
    )

    validate_knowledge_quality_review(
        review,
        fact_count=fact_count,
        candidate_count=candidate_count,
    )

    return review


class WebDesignKnowledgeQualityReviewer:
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
        allow_api: bool = False,
    ) -> dict[str, Any]:
        facts = knowledge.get(
            "facts",
            [],
        )

        if not isinstance(
            facts,
            list,
        ):
            raise ValueError(
                "knowledge facts must be a list"
            )

        candidate_facts = knowledge.get(
            "candidateFacts",
            [],
        )

        if not isinstance(
            candidate_facts,
            list,
        ):
            raise ValueError(
                "knowledge candidateFacts "
                "must be a list"
            )

        prompt = build_knowledge_quality_prompt(
            knowledge=knowledge,
        )

        response = self.ai_client.generate(
            prompt=prompt,
            allow_api=allow_api,
        )

        return (
            parse_knowledge_quality_response(
                response,
                fact_count=len(facts),
                candidate_count=(
                    len(candidate_facts)
                ),
            )
        )
