from __future__ import annotations

from typing import Dict, Tuple, Type

from tools.question_builder.generators.base_generator import BaseGenerator


GeneratorKey = Tuple[str, str]


class GeneratorRegistry:
    def __init__(self) -> None:
        self._registry: Dict[
            GeneratorKey,
            Type[BaseGenerator],
        ] = {}

    def register(
        self,
        *,
        exam: str,
        mode: str,
        generator_class: Type[BaseGenerator],
    ) -> None:

        key = (
            exam.lower(),
            mode.lower(),
        )

        if key in self._registry:
            raise ValueError(
                f"Generator already registered: {key}"
            )

        self._registry[key] = generator_class

    def get(
        self,
        *,
        exam: str,
        mode: str,
    ) -> Type[BaseGenerator]:

        key = (
            exam.lower(),
            mode.lower(),
        )

        try:
            return self._registry[key]
        except KeyError:
            raise ValueError(
                f"Unknown generator: {key}"
            )

    def list_generators(self):
        return sorted(self._registry.keys())


registry = GeneratorRegistry()