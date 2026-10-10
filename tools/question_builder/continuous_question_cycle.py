from __future__ import annotations

import json
from typing import Any, Callable, Optional

from tools.question_builder.continuous_quality_reviewer import (
    ContinuousQualityReviewer,
    validate_quality_review,
)
from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)
from tools.question_builder.generators.webdesign_question_generator import (
    WebDesignQuestionGenerator,
)
from tools.question_builder.prompt_builder import (
    build_rag_question_generation_prompt,
)
from tools.question_builder.validators.webdesign_validator import (
    validate_webdesign_generated_question,
)


QUALITY_PASS_FIELDS = (
    "factualAccuracy",
    "answerUniqueness",
    "grounding",
    "distractorQuality",
    "explanationQuality",
)


def normalize_quality_review_for_target(
    review: dict[str, Any],
    *,
    target_difficulty: int,
) -> dict[str, Any]:
    validate_quality_review(
        review
    )

    normalized = dict(
        review
    )

    normalized[
        "issues"
    ] = list(
        review["issues"]
    )

    normalized[
        "revisionInstructions"
    ] = list(
        review[
            "revisionInstructions"
        ]
    )

    estimate = normalized[
        "difficultyEstimate"
    ]

    exact_match = (
        estimate
        == target_difficulty
    )

    normalized[
        "difficultyMatch"
    ] = exact_match

    if not exact_match:
        issue = (
            "推定難易度 "
            f"{estimate} が今回の目標難易度 "
            f"{target_difficulty} "
            "と一致していない。"
        )

        instruction = (
            "Knowledgeの範囲内で、"
            f"難易度{target_difficulty}に"
            "到達するよう問題構造を"
            "作り直す。"
        )

        if issue not in normalized[
            "issues"
        ]:
            normalized[
                "issues"
            ].append(
                issue
            )

        if instruction not in normalized[
            "revisionInstructions"
        ]:
            normalized[
                "revisionInstructions"
            ].append(
                instruction
            )

        if (
            normalized["decision"]
            == "pass"
        ):
            normalized[
                "decision"
            ] = "revise"

    return normalized


def quality_review_passes(
    review: dict[str, Any],
    *,
    target_difficulty: int,
) -> bool:
    validate_quality_review(
        review
    )

    if review["decision"] != "pass":
        return False

    if (
        review[
            "difficultyEstimate"
        ]
        != target_difficulty
    ):
        return False

    if (
        review["difficultyMatch"]
        is not True
    ):
        return False

    return all(
        review[field] == "pass"
        for field in QUALITY_PASS_FIELDS
    )


def build_revision_prompt(
    *,
    base_prompt: str,
    previous_question: dict[str, Any],
    review: dict[str, Any],
) -> str:
    validate_quality_review(
        review
    )

    instructions = review.get(
        "revisionInstructions",
        [],
    )

    issues = review.get(
        "issues",
        [],
    )

    revision_payload = {
        "previousQuestion": (
            previous_question
        ),
        "qualityReview": {
            "difficultyEstimate": (
                review[
                    "difficultyEstimate"
                ]
            ),
            "difficultyMatch": (
                review[
                    "difficultyMatch"
                ]
            ),
            "issues": issues,
            "revisionInstructions": (
                instructions
            ),
        },
    }

    payload_text = json.dumps(
        revision_payload,
        ensure_ascii=False,
        indent=2,
    )

    return (
        base_prompt
        + "\n\n"
        + "===== 前回問題の品質審査結果 =====\n"
        + "前回問題は品質基準を満たしていません。\n"
        + "以下の審査結果をすべて考慮して、"
        + "問題を作り直してください。\n"
        + "単なる言い換えではなく、"
        + "指摘された原因そのものを改善してください。\n"
        + "事実の根拠として使用してよいのは、"
        + "元のKnowledgeだけです。\n"
        + "新しい専門知識や事実を追加してはいけません。\n"
        + "元の出力JSON形式を厳守してください。\n\n"
        + payload_text
    )


def classify_exhaustion(
    *,
    attempts: list[dict[str, Any]],
    target_difficulty: int,
) -> str:
    if not attempts:
        return "no_attempts"

    reviews = [
        attempt["review"]
        for attempt in attempts
    ]

    grounding_remained_valid = all(
        review["factualAccuracy"] == "pass"
        and review["answerUniqueness"] == "pass"
        and review["grounding"] == "pass"
        and review["explanationQuality"] == "pass"
        for review in reviews
    )

    difficulty_remained_below_target = all(
        review["difficultyEstimate"]
        < target_difficulty
        for review in reviews
    )

    if (
        grounding_remained_valid
        and difficulty_remained_below_target
    ):
        return (
            "knowledge_difficulty_ceiling"
        )

    return "quality_exhausted"


def _validate_cycle_request(
    *,
    knowledge: dict[str, Any],
    section: str,
    difficulty_min: int,
    difficulty_max: int,
    target_difficulty: int,
    question_type: str,
    max_attempts: int,
) -> None:
    if not isinstance(
        knowledge,
        dict,
    ):
        raise ValueError(
            "knowledge must be an object"
        )

    knowledge_id = knowledge.get(
        "id"
    )

    if (
        not isinstance(
            knowledge_id,
            str,
        )
        or not knowledge_id.strip()
    ):
        raise ValueError(
            "knowledge requires id"
        )

    if max_attempts <= 0:
        raise ValueError(
            "max_attempts must be greater than zero"
        )

    if difficulty_min > difficulty_max:
        raise ValueError(
            "difficulty_min must not exceed "
            "difficulty_max"
        )

    if not (
        difficulty_min
        <= target_difficulty
        <= difficulty_max
    ):
        raise ValueError(
            "target_difficulty must be inside "
            "the requested difficulty range"
        )

    profile = get_exam_generation_profile(
        "webdesign"
    )

    if section not in profile[
        "sections"
    ]:
        raise ValueError(
            f"unsupported section: {section}"
        )

    if question_type not in profile[
        "questionTypes"
    ]:
        raise ValueError(
            "unsupported question_type: "
            f"{question_type}"
        )


def _normalize_cycle_knowledge_items(
    *,
    knowledge: dict[str, Any],
    knowledge_items: Optional[
        list[dict[str, Any]]
    ],
    section: str,
) -> list[dict[str, Any]]:
    items = (
        list(
            knowledge_items
        )
        if knowledge_items is not None
        else [
            knowledge
        ]
    )

    if not items:
        raise ValueError(
            "knowledge_items must not be empty"
        )

    if not all(
        isinstance(
            item,
            dict,
        )
        for item in items
    ):
        raise ValueError(
            "knowledge_items must contain "
            "objects"
        )

    knowledge_ids = []

    for item in items:
        knowledge_id = str(
            item.get(
                "id",
                "",
            )
        ).strip()

        if not knowledge_id:
            raise ValueError(
                "each Knowledge item "
                "requires id"
            )

        item_section = str(
            item.get(
                "section",
                "",
            )
        ).strip()

        if (
            item_section
            and item_section
            != section
        ):
            raise ValueError(
                "all Knowledge items must "
                "match the requested section"
            )

        knowledge_ids.append(
            knowledge_id
        )

    if (
        len(
            set(
                knowledge_ids
            )
        )
        != len(
            knowledge_ids
        )
    ):
        raise ValueError(
            "knowledge_items must not "
            "contain duplicate ids"
        )

    primary_id = str(
        knowledge.get(
            "id",
            "",
        )
    ).strip()

    if primary_id not in knowledge_ids:
        raise ValueError(
            "primary knowledge must be "
            "included in knowledge_items"
        )

    return items


def run_webdesign_question_cycle(
    *,
    knowledge: dict[str, Any],
    section: str,
    difficulty_min: int,
    difficulty_max: int,
    target_difficulty: int,
    question_type: str,
    knowledge_items: Optional[
        list[dict[str, Any]]
    ] = None,
    max_attempts: int = 3,
    allow_api: bool = False,
    use_cache: bool = False,
    generator_factory: Optional[
        Callable[[], Any]
    ] = None,
    reviewer_factory: Optional[
        Callable[[], Any]
    ] = None,
) -> dict[str, Any]:
    _validate_cycle_request(
        knowledge=knowledge,
        section=section,
        difficulty_min=(
            difficulty_min
        ),
        difficulty_max=(
            difficulty_max
        ),
        target_difficulty=(
            target_difficulty
        ),
        question_type=question_type,
        max_attempts=max_attempts,
    )

    cycle_knowledge_items = (
        _normalize_cycle_knowledge_items(
            knowledge=knowledge,
            knowledge_items=(
                knowledge_items
            ),
            section=section,
        )
    )

    profile = get_exam_generation_profile(
        "webdesign"
    )

    knowledge_id = knowledge[
        "id"
    ]

    allowed_ids = [
        item["id"]
        for item
        in cycle_knowledge_items
    ]

    combined_keywords = []
    seen_keywords = set()

    for item in cycle_knowledge_items:
        for raw_keyword in item.get(
            "keywords",
            [],
        ):
            keyword = str(
                raw_keyword
            ).strip()

            if (
                not keyword
                or keyword
                in seen_keywords
            ):
                continue

            seen_keywords.add(
                keyword
            )

            combined_keywords.append(
                keyword
            )

    base_prompt = (
        build_rag_question_generation_prompt(
            exam="webdesign",
            section=section,
            section_display_name=(
                profile["sections"][
                    section
                ]
            ),
            difficulty=(
                target_difficulty
            ),
            count=1,
            keywords=combined_keywords,
            knowledge_items=(
                cycle_knowledge_items
            ),
            question_type=(
                question_type
            ),
        )
    )

    if (
        len(
            cycle_knowledge_items
        )
        > 1
    ):
        base_prompt += (
            "\n\n"
            "【複合問題の追加条件】\n"
            "・渡されたKnowledgeをすべて、"
            "正答またはその判断過程に"
            "実質的に使用すること\n"
            "・sourceKnowledgeIdsには"
            "渡されたKnowledge IDを"
            "すべて含めること\n"
            "・各選択肢には、"
            "各Knowledgeに由来する"
            "判断要素を少なくとも1つずつ"
            "含めること\n"
            "・任意の1件のKnowledgeだけを"
            "使った場合には、"
            "正答を一意に決められない"
            "構成にすること\n"
            "・1件のKnowledgeだけで"
            "選択肢を評価した場合、"
            "最低2つの候補が残り、"
            "すべてのKnowledgeを"
            "組み合わせた場合にだけ"
            "正答が1つに決まるようにすること\n"
            "・正答は、"
            "すべてのKnowledge由来の条件を"
            "同時に満たす唯一の選択肢にすること\n"
            "・誤答選択肢は、"
            "すべてが明らかに誤りではなく、"
            "一部の条件は正しいが"
            "少なくとも1条件が誤っている"
            "構造にすること\n"
            "・複数の状況または複数条件を"
            "照合して判断させること\n"
            "・単なる用語と番号の"
            "一対一対応表にしないこと\n"
            "・正解値と誤答値を"
            "機械的に入れ替えただけの"
            "選択肢にしないこと\n"
            "・複数Knowledgeを単に"
            "問題文や選択肢へ並べるだけの"
            "問題にしないこと\n"
            "・目標難易度が4以上の場合、"
            "単純暗記だけでは即答できず、"
            "複数条件の全照合が必要な"
            "問題構造にすること"
        )

    if generator_factory is None:
        generator_factory = (
            WebDesignQuestionGenerator
        )

    if reviewer_factory is None:
        reviewer_factory = (
            ContinuousQualityReviewer
        )

    attempts = []

    previous_question = None
    previous_review = None

    for attempt_number in range(
        1,
        max_attempts + 1,
    ):
        if (
            previous_question is None
            or previous_review is None
        ):
            prompt = base_prompt
        else:
            prompt = build_revision_prompt(
                base_prompt=base_prompt,
                previous_question=(
                    previous_question
                ),
                review=previous_review,
            )

        generator = (
            generator_factory()
        )

        generated = generator.generate(
            {
                "prompt": prompt,
                "expected_count": 1,
                "question_type": (
                    question_type
                ),
                "allowed_source_knowledge_ids": (
                    allowed_ids
                ),
            },
            allow_api=allow_api,
            use_cache=use_cache,
        )

        if (
            not isinstance(
                generated,
                list,
            )
            or len(generated) != 1
            or not isinstance(
                generated[0],
                dict,
            )
        ):
            raise ValueError(
                "generator must return "
                "exactly one question"
            )

        question = generated[0]

        validate_webdesign_generated_question(
            question,
            index=1,
            expected_question_type=(
                question_type
            ),
            allowed_source_knowledge_ids=(
                allowed_ids
            ),
            required_source_knowledge_ids=(
                allowed_ids
                if len(
                    allowed_ids
                )
                > 1
                else None
            ),
        )

        reviewer = (
            reviewer_factory()
        )

        review = reviewer.review(
            knowledge=(
                cycle_knowledge_items
                if len(
                    cycle_knowledge_items
                )
                > 1
                else knowledge
            ),
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
            allow_api=allow_api,
        )

        validate_quality_review(
            review
        )

        review = (
            normalize_quality_review_for_target(
                review,
                target_difficulty=(
                    target_difficulty
                ),
            )
        )

        if quality_review_passes(
            review,
            target_difficulty=(
                target_difficulty
            ),
        ):
            effective_decision = "pass"
        elif (
            review["decision"]
            == "reject"
        ):
            effective_decision = (
                "reject"
            )
        else:
            effective_decision = (
                "revise"
            )

        attempts.append(
            {
                "attempt": (
                    attempt_number
                ),
                "question": question,
                "review": review,
                "effectiveDecision": (
                    effective_decision
                ),
            }
        )

        if (
            effective_decision
            == "pass"
        ):
            return {
                "status": "pass",
                "knowledgeId": (
                    knowledge_id
                ),
                "knowledgeIds": list(
                    allowed_ids
                ),
                "section": section,
                "targetDifficulty": (
                    target_difficulty
                ),
                "questionType": (
                    question_type
                ),
                "attemptsUsed": (
                    attempt_number
                ),
                "attempts": attempts,
                "finalQuestion": (
                    question
                ),
                "finalReview": review,
            }

        if (
            effective_decision
            == "reject"
        ):
            return {
                "status": "rejected",
                "knowledgeId": (
                    knowledge_id
                ),
                "knowledgeIds": list(
                    allowed_ids
                ),
                "section": section,
                "targetDifficulty": (
                    target_difficulty
                ),
                "questionType": (
                    question_type
                ),
                "attemptsUsed": (
                    attempt_number
                ),
                "attempts": attempts,
                "finalQuestion": None,
                "finalReview": review,
            }

        previous_question = (
            question
        )

        previous_review = review

    return {
        "status": "exhausted",
        "exhaustedReason": (
            classify_exhaustion(
                attempts=attempts,
                target_difficulty=(
                    target_difficulty
                ),
            )
        ),
        "knowledgeId": knowledge_id,
        "knowledgeIds": list(
            allowed_ids
        ),
        "section": section,
        "targetDifficulty": (
            target_difficulty
        ),
        "questionType": (
            question_type
        ),
        "attemptsUsed": (
            max_attempts
        ),
        "attempts": attempts,
        "finalQuestion": None,
        "finalReview": (
            attempts[-1]["review"]
            if attempts
            else None
        ),
    }
