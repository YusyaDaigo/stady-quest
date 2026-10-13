import os
from typing import Optional


MODEL_PROFILES = {
    "economy": {
        "text": "gpt-6-luna",
        "vision": "gpt-5.4-mini",
    },
    "quality": {
        "text": "gpt-5.5",
        "vision": "gpt-5.5",
    },
}


def get_model(
    purpose: str,
    *,
    mode: Optional[str] = None,
) -> str:
    selected_mode = (
        os.getenv(
            "STUDY_QUEST_MODEL_MODE",
            "economy",
        )
        if mode is None
        else mode
    )

    if selected_mode not in MODEL_PROFILES:
        raise ValueError(
            f"Unsupported model mode: {selected_mode}"
        )

    profile = MODEL_PROFILES[selected_mode]

    if purpose not in profile:
        raise ValueError(
            f"Unsupported model purpose: {purpose}"
        )

    return profile[purpose]
