from __future__ import annotations

from copy import deepcopy
from typing import Any


DEFAULT_RECENT_LIMIT = 5


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

    candidates = [
        item
        for item in knowledge_items
        if is_plannable_knowledge(
            item,
            section=section,
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
