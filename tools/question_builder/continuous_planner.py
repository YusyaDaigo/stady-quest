from __future__ import annotations

from copy import deepcopy
from typing import Any


DEFAULT_RECENT_LIMIT = 5
DEFAULT_DIFFICULTY_CEILING_EVIDENCE_REQUIRED = 2


def normalize_section(
    value: str,
) -> str:
    return (
        str(value)
        .strip()
        .lower()
    )


def create_planner_state() -> dict[str, Any]:
    return {
        "knowledgeUsage": {},
        "recentKnowledgeIds": [],
        "lastKnowledgeId": None,
        "blockedKnowledgeIds": [],
        "difficultyUsage": {},
        "knowledgeDifficulty": {},
    }


def is_plannable_knowledge(
    item: dict[str, Any],
    *,
    section: str,
) -> bool:
    if not isinstance(
        item,
        dict,
    ):
        return False

    knowledge_id = item.get(
        "id"
    )

    if not isinstance(
        knowledge_id,
        str,
    ) or not knowledge_id.strip():
        return False

    item_section = (
        normalize_section(
            item.get(
                "section",
                "",
            )
        )
    )

    if item_section != (
        normalize_section(
            section
        )
    ):
        return False

    text = str(
        item.get(
            "text",
            "",
        )
    ).strip()

    if not text:
        return False

    review_status = (
        item.get(
            "reviewStatus"
        )
    )

    if (
        review_status is not None
        and str(
            review_status
        ).strip().lower()
        != "approved"
    ):
        return False

    if (
        item.get(
            "questionGenerationEligible"
        )
        is False
    ):
        return False

    return True


def _normalize_usage_count(
    value: Any,
) -> int:
    try:
        count = int(
            value
        )
    except (
        TypeError,
        ValueError,
    ):
        return 0

    return max(
        0,
        count,
    )


def block_knowledge(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
) -> dict[str, Any]:
    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    state = deepcopy(
        planner_state
        or create_planner_state()
    )

    raw_blocked = state.get(
        "blockedKnowledgeIds",
        [],
    )

    blocked = (
        [
            str(item).strip()
            for item in raw_blocked
            if str(item).strip()
        ]
        if isinstance(
            raw_blocked,
            list,
        )
        else []
    )

    if normalized_id not in blocked:
        blocked.append(
            normalized_id
        )

    state[
        "blockedKnowledgeIds"
    ] = blocked

    return state


def _validate_difficulty_range(
    difficulty_min: int,
    difficulty_max: int,
) -> None:
    if (
        not isinstance(
            difficulty_min,
            int,
        )
        or isinstance(
            difficulty_min,
            bool,
        )
    ):
        raise ValueError(
            "difficulty_min must be an integer"
        )

    if (
        not isinstance(
            difficulty_max,
            int,
        )
        or isinstance(
            difficulty_max,
            bool,
        )
    ):
        raise ValueError(
            "difficulty_max must be an integer"
        )

    if difficulty_min > difficulty_max:
        raise ValueError(
            "difficulty_min must not exceed "
            "difficulty_max"
        )


def _normalize_difficulty_counts(
    value: Any,
) -> dict[str, int]:
    if not isinstance(
        value,
        dict,
    ):
        return {}

    normalized = {}

    for raw_level, raw_count in value.items():
        try:
            level = int(
                raw_level
            )

            count = int(
                raw_count
            )
        except (
            TypeError,
            ValueError,
        ):
            continue

        if count <= 0:
            continue

        normalized[
            str(level)
        ] = count

    return normalized


def select_target_difficulty(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    *,
    difficulty_min: int,
    difficulty_max: int,
) -> int:
    _validate_difficulty_range(
        difficulty_min,
        difficulty_max,
    )

    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    state = (
        planner_state
        or create_planner_state()
    )

    raw_knowledge_difficulty = state.get(
        "knowledgeDifficulty",
        {},
    )

    knowledge_difficulty = (
        raw_knowledge_difficulty
        if isinstance(
            raw_knowledge_difficulty,
            dict,
        )
        else {}
    )

    record = knowledge_difficulty.get(
        normalized_id,
        {},
    )

    if not isinstance(
        record,
        dict,
    ):
        record = {}

    pass_counts = (
        _normalize_difficulty_counts(
            record.get(
                "passCounts",
                {},
            )
        )
    )

    blocked_from = record.get(
        "blockedFrom"
    )

    try:
        blocked_from = (
            int(
                blocked_from
            )
            if blocked_from is not None
            else None
        )
    except (
        TypeError,
        ValueError,
    ):
        blocked_from = None

    available = [
        difficulty
        for difficulty in range(
            difficulty_min,
            difficulty_max + 1,
        )
        if (
            blocked_from is None
            or difficulty
            < blocked_from
        )
    ]

    if not available:
        raise ValueError(
            "No available difficulty found "
            f"for Knowledge: {normalized_id}"
        )

    unconfirmed = [
        difficulty
        for difficulty in available
        if pass_counts.get(
            str(
                difficulty
            ),
            0,
        )
        == 0
    ]

    if unconfirmed:
        return min(
            unconfirmed
        )

    return min(
        available,
        key=lambda difficulty: (
            pass_counts.get(
                str(
                    difficulty
                ),
                0,
            ),
            -difficulty,
        ),
    )


def record_difficulty_pass(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    difficulty: int,
) -> dict[str, Any]:
    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    if (
        not isinstance(
            difficulty,
            int,
        )
        or isinstance(
            difficulty,
            bool,
        )
    ):
        raise ValueError(
            "difficulty must be an integer"
        )

    state = deepcopy(
        planner_state
        or create_planner_state()
    )

    knowledge_difficulty = state.get(
        "knowledgeDifficulty"
    )

    if not isinstance(
        knowledge_difficulty,
        dict,
    ):
        knowledge_difficulty = {}

    record = knowledge_difficulty.get(
        normalized_id,
        {},
    )

    if not isinstance(
        record,
        dict,
    ):
        record = {}

    pass_counts = (
        _normalize_difficulty_counts(
            record.get(
                "passCounts",
                {},
            )
        )
    )

    key = str(
        difficulty
    )

    pass_counts[key] = (
        pass_counts.get(
            key,
            0,
        )
        + 1
    )

    record[
        "passCounts"
    ] = pass_counts

    ceiling_evidence = (
        _normalize_difficulty_counts(
            record.get(
                "ceilingEvidence",
                {},
            )
        )
    )

    ceiling_evidence.pop(
        key,
        None,
    )

    if ceiling_evidence:
        record[
            "ceilingEvidence"
        ] = ceiling_evidence
    else:
        record.pop(
            "ceilingEvidence",
            None,
        )

    blocked_from = record.get(
        "blockedFrom"
    )

    try:
        blocked_from = (
            int(
                blocked_from
            )
            if blocked_from is not None
            else None
        )
    except (
        TypeError,
        ValueError,
    ):
        blocked_from = None

    if (
        blocked_from is not None
        and difficulty
        >= blocked_from
    ):
        record.pop(
            "blockedFrom",
            None,
        )

    knowledge_difficulty[
        normalized_id
    ] = record

    difficulty_usage = state.get(
        "difficultyUsage"
    )

    if not isinstance(
        difficulty_usage,
        dict,
    ):
        difficulty_usage = {}

    difficulty_usage[key] = (
        _normalize_usage_count(
            difficulty_usage.get(
                key,
                0,
            )
        )
        + 1
    )

    state[
        "knowledgeDifficulty"
    ] = knowledge_difficulty

    state[
        "difficultyUsage"
    ] = difficulty_usage

    return state


def get_difficulty_ceiling_evidence_count(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    difficulty: int,
) -> int:
    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    state = (
        planner_state
        or create_planner_state()
    )

    knowledge_difficulty = state.get(
        "knowledgeDifficulty",
        {},
    )

    if not isinstance(
        knowledge_difficulty,
        dict,
    ):
        return 0

    record = knowledge_difficulty.get(
        normalized_id,
        {},
    )

    if not isinstance(
        record,
        dict,
    ):
        return 0

    evidence = (
        _normalize_difficulty_counts(
            record.get(
                "ceilingEvidence",
                {},
            )
        )
    )

    return evidence.get(
        str(
            difficulty
        ),
        0,
    )


def get_difficulty_ceiling_status(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    difficulty: int,
) -> str:
    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    state = (
        planner_state
        or create_planner_state()
    )

    knowledge_difficulty = state.get(
        "knowledgeDifficulty",
        {},
    )

    record = (
        knowledge_difficulty.get(
            normalized_id,
            {},
        )
        if isinstance(
            knowledge_difficulty,
            dict,
        )
        else {}
    )

    if not isinstance(
        record,
        dict,
    ):
        record = {}

    pass_counts = (
        _normalize_difficulty_counts(
            record.get(
                "passCounts",
                {},
            )
        )
    )

    if (
        pass_counts.get(
            str(
                difficulty
            ),
            0,
        )
        > 0
    ):
        return "ignored"

    blocked_from = record.get(
        "blockedFrom"
    )

    try:
        blocked_from = (
            int(
                blocked_from
            )
            if blocked_from is not None
            else None
        )
    except (
        TypeError,
        ValueError,
    ):
        blocked_from = None

    if (
        blocked_from is not None
        and blocked_from
        <= difficulty
    ):
        return "recorded"

    evidence_count = (
        get_difficulty_ceiling_evidence_count(
            state,
            normalized_id,
            difficulty,
        )
    )

    if evidence_count > 0:
        return "pending"

    return "none"


def record_difficulty_ceiling(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    difficulty: int,
    *,
    difficulty_min: int,
    required_evidence: int = (
        DEFAULT_DIFFICULTY_CEILING_EVIDENCE_REQUIRED
    ),
) -> dict[str, Any]:
    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    if (
        not isinstance(
            difficulty,
            int,
        )
        or isinstance(
            difficulty,
            bool,
        )
    ):
        raise ValueError(
            "difficulty must be an integer"
        )

    if (
        not isinstance(
            required_evidence,
            int,
        )
        or isinstance(
            required_evidence,
            bool,
        )
        or required_evidence < 1
    ):
        raise ValueError(
            "required_evidence must be "
            "a positive integer"
        )

    state = deepcopy(
        planner_state
        or create_planner_state()
    )

    knowledge_difficulty = state.get(
        "knowledgeDifficulty"
    )

    if not isinstance(
        knowledge_difficulty,
        dict,
    ):
        knowledge_difficulty = {}

    record = knowledge_difficulty.get(
        normalized_id,
        {},
    )

    if not isinstance(
        record,
        dict,
    ):
        record = {}

    pass_counts = (
        _normalize_difficulty_counts(
            record.get(
                "passCounts",
                {},
            )
        )
    )

    key = str(
        difficulty
    )

    if (
        pass_counts.get(
            key,
            0,
        )
        > 0
    ):
        ceiling_evidence = (
            _normalize_difficulty_counts(
                record.get(
                    "ceilingEvidence",
                    {},
                )
            )
        )

        ceiling_evidence.pop(
            key,
            None,
        )

        if ceiling_evidence:
            record[
                "ceilingEvidence"
            ] = ceiling_evidence
        else:
            record.pop(
                "ceilingEvidence",
                None,
            )

        knowledge_difficulty[
            normalized_id
        ] = record

        state[
            "knowledgeDifficulty"
        ] = knowledge_difficulty

        return state

    old_blocked_from = record.get(
        "blockedFrom"
    )

    try:
        old_blocked_from = (
            int(
                old_blocked_from
            )
            if old_blocked_from is not None
            else None
        )
    except (
        TypeError,
        ValueError,
    ):
        old_blocked_from = None

    if (
        old_blocked_from is not None
        and old_blocked_from
        <= difficulty
    ):
        return state

    ceiling_evidence = (
        _normalize_difficulty_counts(
            record.get(
                "ceilingEvidence",
                {},
            )
        )
    )

    ceiling_evidence[
        key
    ] = (
        ceiling_evidence.get(
            key,
            0,
        )
        + 1
    )

    record[
        "ceilingEvidence"
    ] = ceiling_evidence

    knowledge_difficulty[
        normalized_id
    ] = record

    state[
        "knowledgeDifficulty"
    ] = knowledge_difficulty

    if (
        ceiling_evidence[key]
        < required_evidence
    ):
        return state

    new_blocked_from = (
        difficulty
        if old_blocked_from is None
        else min(
            old_blocked_from,
            difficulty,
        )
    )

    record[
        "blockedFrom"
    ] = new_blocked_from

    knowledge_difficulty[
        normalized_id
    ] = record

    state[
        "knowledgeDifficulty"
    ] = knowledge_difficulty

    if difficulty <= difficulty_min:
        state = block_knowledge(
            state,
            normalized_id,
        )

    return state


def rank_knowledge_candidates(
    knowledge_items: list[
        dict[str, Any]
    ],
    *,
    section: str,
    planner_state: dict[
        str,
        Any,
    ] | None = None,
    recent_limit: int = (
        DEFAULT_RECENT_LIMIT
    ),
) -> list[dict[str, Any]]:
    if recent_limit < 0:
        raise ValueError(
            "recent_limit must not be negative"
        )

    state = (
        planner_state
        or create_planner_state()
    )

    raw_usage = state.get(
        "knowledgeUsage",
        {},
    )

    usage = (
        raw_usage
        if isinstance(
            raw_usage,
            dict,
        )
        else {}
    )

    raw_recent = state.get(
        "recentKnowledgeIds",
        [],
    )

    recent = (
        [
            str(
                knowledge_id
            )
            for knowledge_id
            in raw_recent
        ]
        if isinstance(
            raw_recent,
            list,
        )
        else []
    )

    if recent_limit == 0:
        recent = []
    else:
        recent = (
            recent[
                -recent_limit:
            ]
        )

    recent_set = set(
        recent
    )

    raw_blocked = state.get(
        "blockedKnowledgeIds",
        [],
    )

    blocked = (
        [
            str(
                knowledge_id
            ).strip()
            for knowledge_id
            in raw_blocked
            if str(
                knowledge_id
            ).strip()
        ]
        if isinstance(
            raw_blocked,
            list,
        )
        else []
    )

    blocked_set = set(
        blocked
    )

    candidates = [
        item
        for item in knowledge_items
        if (
            is_plannable_knowledge(
                item,
                section=section,
            )
            and item["id"]
            not in blocked_set
        )
    ]

    ranked = sorted(
        candidates,
        key=lambda item: (
            1
            if item["id"]
            in recent_set
            else 0,
            _normalize_usage_count(
                usage.get(
                    item["id"],
                    0,
                )
            ),
            item["id"],
        ),
    )

    return ranked


def select_next_knowledge(
    knowledge_items: list[
        dict[str, Any]
    ],
    *,
    section: str,
    planner_state: dict[
        str,
        Any,
    ] | None = None,
    recent_limit: int = (
        DEFAULT_RECENT_LIMIT
    ),
) -> dict[str, Any]:
    ranked = (
        rank_knowledge_candidates(
            knowledge_items,
            section=section,
            planner_state=(
                planner_state
            ),
            recent_limit=recent_limit,
        )
    )

    if not ranked:
        raise ValueError(
            "No plannable Knowledge found "
            f"for section: {section}"
        )

    return deepcopy(
        ranked[0]
    )


def record_knowledge_use(
    planner_state: dict[
        str,
        Any,
    ] | None,
    knowledge_id: str,
    *,
    recent_limit: int = (
        DEFAULT_RECENT_LIMIT
    ),
) -> dict[str, Any]:
    if recent_limit < 0:
        raise ValueError(
            "recent_limit must not be negative"
        )

    normalized_id = str(
        knowledge_id
    ).strip()

    if not normalized_id:
        raise ValueError(
            "knowledge_id must not be empty"
        )

    state = deepcopy(
        planner_state
        or create_planner_state()
    )

    usage = state.get(
        "knowledgeUsage"
    )

    if not isinstance(
        usage,
        dict,
    ):
        usage = {}

    usage[
        normalized_id
    ] = (
        _normalize_usage_count(
            usage.get(
                normalized_id,
                0,
            )
        )
        + 1
    )

    recent = state.get(
        "recentKnowledgeIds"
    )

    if not isinstance(
        recent,
        list,
    ):
        recent = []

    recent = [
        str(
            item
        )
        for item in recent
        if str(
            item
        ).strip()
    ]

    recent.append(
        normalized_id
    )

    if recent_limit == 0:
        recent = []
    else:
        recent = (
            recent[
                -recent_limit:
            ]
        )

    state[
        "knowledgeUsage"
    ] = usage

    state[
        "recentKnowledgeIds"
    ] = recent

    state[
        "lastKnowledgeId"
    ] = normalized_id

    return state
