from __future__ import annotations

from typing import NamedTuple, Type

from tools.question_builder.generators.base_generator import (
    BaseGenerator,
)
from tools.question_builder.generators.drone_question_generator import (
    DroneQuestionGenerator,
)
from tools.question_builder.generators.pharmacy_similar_generator import (
    PharmacySimilarGenerator,
)
from tools.question_builder.generators.webdesign_question_generator import (
    WebDesignQuestionGenerator,
)


class GeneratorConfig(NamedTuple):
    exam: str
    mode: str
    generator_class: Type[BaseGenerator]


GENERATOR_CONFIGS = [
    GeneratorConfig(
        exam="drone",
        mode="batch",
        generator_class=DroneQuestionGenerator,
    ),
    GeneratorConfig(
        exam="pharmacy",
        mode="similar",
        generator_class=PharmacySimilarGenerator,
    ),
    GeneratorConfig(
        exam="webdesign",
        mode="batch",
        generator_class=WebDesignQuestionGenerator,
    ),
]
