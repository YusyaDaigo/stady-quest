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
    "objectiveCoverage",
    "factAssessments",
    "issues",
    "recommendedFactIndexes",
}


def validate_knowledge_quality_review(
    review: dict[str, Any],
    *,
    fact_count: int,
    objective_count: int,
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

    objective_coverage = review[
        "objectiveCoverage"
    ]

    if not isinstance(
        objective_coverage,
        list,
    ):
        raise ValueError(
            "objectiveCoverage must be a list"
        )

    if len(
        objective_coverage
    ) != objective_count:
        raise ValueError(
            "objectiveCoverage length must "
            "match learning objective count"
        )

    seen_objective_indexes = set()

    for item in objective_coverage:
        if not isinstance(
            item,
            dict,
        ):
            raise ValueError(
                "objectiveCoverage items "
                "must be objects"
            )

        if set(item) != {
            "objectiveIndex",
            "status",
        }:
            raise ValueError(
                "objectiveCoverage item "
                "has invalid fields"
            )

        objective_index = item[
            "objectiveIndex"
        ]

        if (
            not isinstance(
                objective_index,
                int,
            )
            or isinstance(
                objective_index,
                bool,
            )
            or not (
                0
                <= objective_index
                < objective_count
            )
        ):
            raise ValueError(
                "invalid objectiveIndex"
            )

        if (
            objective_index
            in seen_objective_indexes
        ):
            raise ValueError(
                "duplicate objectiveIndex"
            )

        seen_objective_indexes.add(
            objective_index
        )

        if item["status"] not in {
            "supported",
            "partial",
            "unsupported",
        }:
            raise ValueError(
                "invalid objectiveCoverage status"
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
            "useful_background",
            "unrelated",
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

    usable_indexes = sorted(
        item["factIndex"]
        for item in fact_assessments
        if item["relevance"] in {
            "direct",
            "useful_background",
        }
    )

    if indexes != usable_indexes:
        raise ValueError(
            "recommendedFactIndexes must "
            "exactly match usable facts"
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
            for item in objective_coverage
        ):
            raise ValueError(
                "pass requires all learning "
                "objectives to be supported"
            )

        if any(
            item["relevance"]
            == "unrelated"
            for item in fact_assessments
        ):
            raise ValueError(
                "pass cannot contain unrelated "
                "verified facts"
            )


def build_knowledge_quality_prompt(
    *,
    knowledge: dict[str, Any],
) -> str:
    payload = {
        "id": knowledge.get("id"),
        "section": knowledge.get("section"),
        "title": knowledge.get("title"),
        "sourceSummary": knowledge.get(
            "sourceSummary"
        ),
        "learningObjectives": knowledge.get(
            "learningObjectives",
            [],
        ),
        "sourceObservations": knowledge.get(
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
title、sourceSummary、
learningObjectivesが示す
中心学習論点とverifiedFactsが
一致しているか。

answerSupport:
learningObjectivesを達成するための
根拠がverifiedFactsに
十分含まれているか。

sourceObservations:
問題画像から抽出された
設問・選択肢・出題形式などの
観察情報です。

sourceObservations自体が
verifiedFactsによって再度
証明される必要はありません。

sourceObservationsにしか存在しない
選択肢名や表現があることだけを理由に
holdやrejectにしてはいけません。

objectiveCoverage:
learningObjectivesを
0始まりindexごとに必ず全件評価し、
verifiedFactsによる支援状況を
次のいずれかで示してください。

- supported:
  学習目標を十分に支える
- partial:
  一部は支えるが情報不足がある
- unsupported:
  学習目標を支える根拠がない

factScope:
verifiedFactsを、
元の学習論点との関係で評価してください。

factAssessments:
verifiedFactsを0始まりindexごとに
必ず全件評価してください。

relevance:
- direct:
  learningObjectivesを直接支える事実
- useful_background:
  学習目標に直接必須ではないが、
  同じ論点の理解・解説・問題生成に
  有用な周辺知識
- unrelated:
  元の学習論点から外れており、
  Knowledge生成に使用すべきでない事実

同じ分野であるという理由だけで
useful_backgroundにしてはいけません。

sectionConsistency:
section、answerSection、
sectionMatchに矛盾がないか。

recommendedFactIndexes:
factAssessmentsで
directまたはuseful_backgroundと
判定したverifiedFactsの
0始まりindexを昇順で指定してください。

decision:

pass:
- 4項目すべてpass
- learningObjectivesがすべてsupported
- unrelatedなverifiedFactがない
- そのまま人間レビュー候補にできる

hold:
- 使用可能な根拠は存在するが、
  learningObjectiveがpartialまたはunsupported、
  unrelatedな事実の混入、
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
  "objectiveCoverage": [
    {{
      "objectiveIndex": 0,
      "status": "supported|partial|unsupported"
    }}
  ],
  "factAssessments": [
    {{
      "factIndex": 0,
      "relevance": "direct|useful_background|unrelated"
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
    objective_count: int,
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
        objective_count=objective_count,
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

        learning_objectives = knowledge.get(
            "learningObjectives",
            [],
        )

        if not isinstance(
            learning_objectives,
            list,
        ):
            raise ValueError(
                "knowledge learningObjectives "
                "must be a list"
            )

        if not learning_objectives:
            raise ValueError(
                "knowledge requires at least "
                "one learning objective"
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
                objective_count=(
                    len(learning_objectives)
                ),
            )
        )
