from __future__ import annotations

from tools.question_builder.generators.base_generator import (
    BaseGenerator,
)
from tools.question_builder.registry.generator_config import (
    GENERATOR_CONFIGS,
)
from tools.question_builder.registry.generator_registry import (
    registry,
)


def register_configured_generators() -> None:
    existing = set(
        registry.list_generators()
    )

    for config in GENERATOR_CONFIGS:
        key = (
            config.exam.lower(),
            config.mode.lower(),
        )

        if key in existing:
            continue

        registry.register(
            exam=config.exam,
            mode=config.mode,
            generator_class=config.generator_class,
        )

        existing.add(key)


register_configured_generators()


def get_generator(
    *,
    exam: str,
    mode: str,
) -> BaseGenerator:
    generator_class = registry.get(
        exam=exam,
        mode=mode,
    )

    return generator_class()
