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


def quality_review_passes(
    review: dict[str, Any],
) -> bool:
    validate_quality_review(
        review
    )

    if review["decision"] != "pass":
        return False

    if review["difficultyMatch"] is not True:
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
    difficulty_min: int,
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
        review["difficultyMatch"] is False
        and review["difficultyEstimate"]
        < difficulty_min
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


def run_webdesign_question_cycle(
    *,
    knowledge: dict[str, Any],
    section: str,
    difficulty_min: int,
    difficulty_max: int,
    target_difficulty: int,
    question_type: str,
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

    profile = get_exam_generation_profile(
        "webdesign"
    )

    knowledge_id = knowledge[
        "id"
    ]

    allowed_ids = [
        knowledge_id
    ]

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
            keywords=knowledge.get(
                "keywords",
                [],
            ),
            knowledge_items=[
                knowledge
            ],
            question_type=(
                question_type
            ),
        )
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
        )

        reviewer = (
            reviewer_factory()
        )

        review = reviewer.review(
            knowledge=knowledge,
            question=question,
            difficulty_min=(
                difficulty_min
            ),
            difficulty_max=(
                difficulty_max
            ),
            allow_api=allow_api,
        )

        validate_quality_review(
            review
        )

        if quality_review_passes(
            review
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
                difficulty_min=(
                    difficulty_min
                ),
            )
        ),
        "knowledgeId": knowledge_id,
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
