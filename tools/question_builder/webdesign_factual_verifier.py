from __future__ import annotations

import json
from typing import Any

from tools.question_builder.core.ai_client import (
    OpenAITextClient,
)


REQUIRED_RESULT_FIELDS = {
    "decision",
    "factAssessments",
    "contextAssessment",
    "issues",
}


def validate_evidence(
    evidence: list[dict[str, Any]],
) -> None:
    if not isinstance(
        evidence,
        list,
    ):
        raise ValueError(
            "evidence must be a list"
        )

    if not evidence:
        raise ValueError(
            "factual verification requires "
            "external evidence"
        )

    for index, item in enumerate(
        evidence
    ):
        if not isinstance(
            item,
            dict,
        ):
            raise ValueError(
                f"evidence {index} must be an object"
            )

        for field in [
            "sourceTitle",
            "sourceUrl",
            "sourceType",
            "excerpt",
        ]:
            value = item.get(
                field
            )

            if (
                not isinstance(
                    value,
                    str,
                )
                or not value.strip()
            ):
                raise ValueError(
                    f"evidence {index} requires "
                    f"{field}"
                )


def validate_factual_result(
    result: dict[str, Any],
    *,
    fact_count: int,
    evidence_count: int,
) -> None:
    if not isinstance(
        result,
        dict,
    ):
        raise ValueError(
            "factual verification result "
            "must be an object"
        )

    missing = (
        REQUIRED_RESULT_FIELDS
        - result.keys()
    )

    if missing:
        raise ValueError(
            "factual verification result "
            "missing fields: "
            f"{sorted(missing)}"
        )

    if fact_count < 1 or evidence_count < 1:
        raise ValueError(
            "fact_count and evidence_count "
            "must be positive"
        )

    if result["decision"] not in {
        "verified",
        "conflict",
        "insufficient",
    }:
        raise ValueError(
            "invalid factual verification decision"
        )

    assessments = result[
        "factAssessments"
    ]

    if not isinstance(
        assessments,
        list,
    ):
        raise ValueError(
            "factAssessments must be a list"
        )

    if len(
        assessments
    ) != fact_count:
        raise ValueError(
            "factAssessments length must "
            "match fact count"
        )

    seen_indexes = set()

    for item in assessments:
        if not isinstance(
            item,
            dict,
        ):
            raise ValueError(
                "factAssessment must be an object"
            )

        if set(item) != {
            "factIndex",
            "status",
            "evidenceIndexes",
        }:
            raise ValueError(
                "factAssessment has invalid fields"
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

        if fact_index in seen_indexes:
            raise ValueError(
                "duplicate factIndex"
            )

        seen_indexes.add(
            fact_index
        )

        if item["status"] not in {
            "verified",
            "conflict",
            "insufficient",
        }:
            raise ValueError(
                "invalid fact status"
            )

        evidence_indexes = item[
            "evidenceIndexes"
        ]

        if not isinstance(
            evidence_indexes,
            list,
        ):
            raise ValueError(
                "evidenceIndexes must be a list"
            )

        if any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or not 0 <= value < evidence_count
            for value in evidence_indexes
        ):
            raise ValueError(
                "invalid evidence index"
            )

        if len(evidence_indexes) != len(
            set(evidence_indexes)
        ):
            raise ValueError(
                "duplicate evidence index"
            )

        if (
            item["status"] in {
                "verified",
                "conflict",
            }
            and not evidence_indexes
        ):
            raise ValueError(
                "verified/conflict requires "
                "at least one evidence index"
            )

    context = result["contextAssessment"]

    if (
        not isinstance(context, dict)
        or set(context) != {
            "status",
            "evidenceIndexes",
            "reason",
        }
    ):
        raise ValueError(
            "invalid contextAssessment structure"
        )

    if context["status"] not in {
        "supported",
        "misleading",
        "insufficient",
    }:
        raise ValueError(
            "invalid context status"
        )

    context_indexes = context["evidenceIndexes"]

    if not isinstance(context_indexes, list):
        raise ValueError(
            "context evidenceIndexes must be a list"
        )

    if any(
        not isinstance(index, int)
        or isinstance(index, bool)
        or not 0 <= index < evidence_count
        for index in context_indexes
    ):
        raise ValueError(
            "invalid context evidence index"
        )

    if len(context_indexes) != len(
        set(context_indexes)
    ):
        raise ValueError(
            "duplicate context evidence index"
        )

    if (
        context["status"] in {
            "supported",
            "misleading",
        }
        and not context_indexes
    ):
        raise ValueError(
            "supported/misleading context "
            "requires evidence"
        )

    if (
        not isinstance(context["reason"], str)
        or not context["reason"].strip()
    ):
        raise ValueError(
            "context requires a reason"
        )

    issues = result[
        "issues"
    ]

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
            "issues must contain "
            "non-empty strings"
        )

    statuses = {
        item["status"]
        for item in assessments
    }

    if "conflict" in statuses:
        expected_decision = "conflict"
    elif "insufficient" in statuses:
        expected_decision = "insufficient"
    else:
        expected_decision = "verified"

    if result["decision"] != expected_decision:
        raise ValueError(
            "overall decision does not match "
            "individual fact assessments"
        )


def build_fact_targets(
    knowledge: dict[str, Any],
) -> list[dict[str, Any]]:
    if not isinstance(knowledge, dict):
        raise ValueError(
            "knowledge must be an object"
        )

    targets = []

    for field, origin in [
        ("candidateFacts", "source"),
        ("facts", "answer"),
    ]:
        values = knowledge.get(field)

        if (
            not isinstance(values, list)
            or not values
        ):
            raise ValueError(
                f"knowledge requires non-empty {field}"
            )

        for original_index, statement in enumerate(
            values
        ):
            if (
                not isinstance(statement, str)
                or not statement.strip()
            ):
                raise ValueError(
                    f"{field}[{original_index}] "
                    "must be a non-empty string"
                )

            targets.append(
                {
                    "factIndex": len(targets),
                    "origin": origin,
                    "originalIndex": original_index,
                    "statement": statement.strip(),
                }
            )

    return targets


def build_factual_verification_prompt(
    *,
    knowledge: dict[str, Any],
    evidence: list[dict[str, Any]],
) -> str:
    validate_evidence(
        evidence
    )

    payload = {
        "id": knowledge.get("id"),
        "title": knowledge.get("title"),
        "sourceSummary": knowledge.get(
            "sourceSummary"
        ),
        "learningObjectives": knowledge.get(
            "learningObjectives",
            [],
        ),
        "factTargets": build_fact_targets(
            knowledge
        ),
    }

    knowledge_json = json.dumps(
        payload,
        ensure_ascii=False,
        indent=2,
    )

    evidence_json = json.dumps(
        evidence,
        ensure_ascii=False,
        indent=2,
    )

    return f"""
あなたはStudy QUESTの
外部事実検証担当です。

目的:
Knowledge候補の事実を、
提示された外部Evidenceだけを根拠に
検証してください。

最重要ルール:
- Evidenceに書かれている内容だけを使用してください。
- あなた自身の一般知識や記憶を使用しないでください。
- Evidenceから確認できない場合は
  insufficientとしてください。
- Knowledge教材や解答冊子の記載を
  正しいものとして前提にしないでください。
- EvidenceとKnowledgeが矛盾する場合は
  conflictとしてください。
- 推測で補完してはいけません。

検証対象:
factTargetsの全件を
factIndexごとに評価してください。

origin=source は問題側の抽出事実、
origin=answer は解答冊子側の抽出事実です。

両者とも未検証の主張として扱ってください。
解答冊子側の記述も正しいと仮定しないでください。

factIndexはfactTargetsに示された番号を使い、
順番を変えたり省略したりしないでください。

文脈評価:
factTargetsの個別評価とは別に、
sourceSummary・learningObjectivesと
解答側factsの関係を評価してください。

特に、個々の記述は正しくても、
解答の根拠として並べることで
誤った範囲・分類・因果関係を
示唆していないか確認してください。

contextAssessment.status:
- supported:
  Evidenceが中心学習論点と解答の関係を支持する
- misleading:
  Evidenceに照らすと説明の使い方が誤解を招く
- insufficient:
  Evidenceだけでは説明の妥当性を判断できない

contextAssessmentにも根拠となる
evidenceIndexesを指定してください。
外部Evidenceのない推測はしないでください。

decisionは従来どおり、
個別factの判定だけを集約してください。
文脈の判定はcontextAssessmentへ
分離してください。

status:
- verified:
  Evidenceが事実を明確に支持する
- conflict:
  Evidenceが事実と明確に矛盾する
- insufficient:
  Evidenceだけでは確認できない

evidenceIndexes:
その判定の根拠となったEvidenceの
0始まりindexを記録してください。

decision:
- verified:
  candidateFactsがすべてverified
- conflict:
  1件以上conflict
- insufficient:
  conflictはないが、
  1件以上insufficient

JSONのみを返してください。

形式:
{{
  "decision": "verified|conflict|insufficient",
  "factAssessments": [
    {{
      "factIndex": 0,
      "status": "verified|conflict|insufficient",
      "evidenceIndexes": [
        0
      ]
    }}
  ],
  "contextAssessment": {{
    "status": "supported|misleading|insufficient",
    "evidenceIndexes": [
      0
    ],
    "reason": "説明文脈に対する評価理由"
  }},
  "issues": [
    "検証上の問題点"
  ]
}}

Knowledge:
{knowledge_json}

External Evidence:
{evidence_json}
""".strip()


def parse_factual_verification_response(
    response_text: str,
    *,
    fact_count: int,
    evidence_count: int,
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

    result = json.loads(
        text
    )

    validate_factual_result(
        result,
        fact_count=fact_count,
        evidence_count=evidence_count,
    )

    return result


class WebDesignFactualVerifier:
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

    def verify(
        self,
        *,
        knowledge: dict[str, Any],
        evidence: list[dict[str, Any]],
        allow_api: bool = False,
    ) -> dict[str, Any]:
        fact_targets = build_fact_targets(
            knowledge
        )

        prompt = (
            build_factual_verification_prompt(
                knowledge=knowledge,
                evidence=evidence,
            )
        )

        response = self.ai_client.generate(
            prompt,
            allow_api=allow_api,
        )

        result = parse_factual_verification_response(
            response,
            fact_count=len(fact_targets),
            evidence_count=len(evidence),
        )

        factual_gate = (
            "pass"
            if (
                result["decision"] == "verified"
                and result["contextAssessment"]["status"]
                == "supported"
            )
            else "hold"
        )

        return {
            **result,
            "factTargets": fact_targets,
            "factualGate": factual_gate,
        }
