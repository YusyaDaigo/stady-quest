import pytest

from tools.question_builder.registry import (
    get_generator,
    registry,
)

from tools.question_builder.generators import (
    DroneQuestionGenerator,
    PharmacySimilarGenerator,
)


def test_factory_returns_drone():

    generator = get_generator(
        exam="drone",
        mode="batch",
    )

    assert isinstance(
        generator,
        DroneQuestionGenerator,
    )


def test_factory_returns_pharmacy():

    generator = get_generator(
        exam="pharmacy",
        mode="similar",
    )

    assert isinstance(
        generator,
        PharmacySimilarGenerator,
    )


def test_unknown_generator():

    with pytest.raises(
        ValueError,
        match="Unknown generator",
    ):
        get_generator(
            exam="unknown",
            mode="batch",
        )


def test_registry_lists_generators():

    generators = registry.list_generators()

    assert (
        "drone",
        "batch",
    ) in generators

    assert (
        "pharmacy",
        "similar",
    ) in generators

def test_generator_configs_contain_expected_generators():
    from tools.question_builder.registry import (
        GENERATOR_CONFIGS,
    )

    config_keys = {
        (
            config.exam,
            config.mode,
        )
        for config in GENERATOR_CONFIGS
    }

    assert (
        "drone",
        "batch",
    ) in config_keys

    assert (
        "pharmacy",
        "similar",
    ) in config_keys


def test_configured_generators_match_registry():
    from tools.question_builder.registry import (
        GENERATOR_CONFIGS,
    )

    registry_keys = set(
        registry.list_generators()
    )

    config_keys = {
        (
            config.exam.lower(),
            config.mode.lower(),
        )
        for config in GENERATOR_CONFIGS
    }

    assert config_keys <= registry_keys


def test_register_configured_generators_is_idempotent():
    from tools.question_builder.registry import (
        register_configured_generators,
    )

    before = registry.list_generators()

    register_configured_generators()
    register_configured_generators()

    after = registry.list_generators()

    assert after == before
