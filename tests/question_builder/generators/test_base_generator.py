from pathlib import Path

import pytest

from tools.question_builder.generators.base_generator import (
    BaseGenerator,
)


class FakeAIClient:
    def __init__(
        self,
        response_text='{"value": 123}',
    ):
        self.response_text = response_text
        self.call_count = 0
        self.last_prompt = None
        self.last_allow_api = None

    def generate(
        self,
        *,
        prompt,
        allow_api,
    ):
        self.call_count += 1
        self.last_prompt = prompt
        self.last_allow_api = allow_api

        return self.response_text


class FailingAIClient:
    def generate(
        self,
        *,
        prompt,
        allow_api,
    ):
        raise AssertionError(
            "AI client must not be called"
        )


class TestGenerator(BaseGenerator):
    __test__ = False

    def __init__(
        self,
        cache_dir: Path,
    ):
        super().__init__(
            model="test-model",
            cache_dir=cache_dir,
            max_api_calls=1,
        )

        self.parse_call_count = 0
        self.cache_validation_count = 0

    def build_prompt(
        self,
        input_data,
    ):
        return input_data.get(
            "prompt",
            ""
        )

    def parse_response(
        self,
        response_text,
        input_data,
    ):
        self.parse_call_count += 1

        return {
            "response": response_text,
            "source": input_data.get(
                "source"
            ),
        }

    def validate_cached_result(
        self,
        cached,
        input_data,
    ):
        self.cache_validation_count += 1

        if not isinstance(cached, dict):
            raise ValueError(
                "cached result must be an object"
            )

        return cached


def test_generate_calls_ai_and_parser(
    tmp_path,
):
    generator = TestGenerator(
        tmp_path
    )
    fake_ai = FakeAIClient(
        response_text="generated response"
    )
    generator.ai_client = fake_ai

    result = generator.generate(
        {
            "prompt": "Generate",
            "source": "test",
        },
        allow_api=True,
        use_cache=False,
    )

    assert result == {
        "response": "generated response",
        "source": "test",
    }
    assert fake_ai.call_count == 1
    assert fake_ai.last_prompt == "Generate"
    assert fake_ai.last_allow_api is True
    assert generator.parse_call_count == 1


def test_generate_saves_and_reuses_cache(
    tmp_path,
):
    first_generator = TestGenerator(
        tmp_path
    )
    first_ai = FakeAIClient(
        response_text="cached response"
    )
    first_generator.ai_client = first_ai

    input_data = {
        "prompt": "Generate",
        "source": "cache-test",
    }

    first_result = first_generator.generate(
        input_data,
        allow_api=True,
        use_cache=True,
    )

    assert first_ai.call_count == 1

    second_generator = TestGenerator(
        tmp_path
    )
    second_generator.ai_client = (
        FailingAIClient()
    )

    second_result = second_generator.generate(
        input_data,
        allow_api=False,
        use_cache=True,
    )

    assert second_result == first_result
    assert (
        second_generator.cache_validation_count
        == 1
    )
    assert (
        second_generator.parse_call_count
        == 0
    )


def test_use_cache_false_skips_cache(
    tmp_path,
):
    generator = TestGenerator(
        tmp_path
    )
    fake_ai = FakeAIClient(
        response_text="fresh"
    )
    generator.ai_client = fake_ai

    input_data = {
        "prompt": "Generate",
    }

    generator.generate(
        input_data,
        allow_api=True,
        use_cache=False,
    )
    generator.generate(
        input_data,
        allow_api=True,
        use_cache=False,
    )

    assert fake_ai.call_count == 2


@pytest.mark.parametrize(
    "input_data",
    [
        None,
        [],
        "invalid",
    ],
)
def test_generate_rejects_non_dictionary_input(
    tmp_path,
    input_data,
):
    generator = TestGenerator(
        tmp_path
    )

    with pytest.raises(
        ValueError,
        match="input_data must be a dictionary",
    ):
        generator.generate(
            input_data,
            use_cache=False,
        )


@pytest.mark.parametrize(
    "prompt",
    [
        "",
        "   ",
        None,
    ],
)
def test_generate_rejects_empty_prompt(
    tmp_path,
    prompt,
):
    generator = TestGenerator(
        tmp_path
    )

    with pytest.raises(
        ValueError,
        match="generated prompt must be",
    ):
        generator.generate(
            {
                "prompt": prompt,
            },
            use_cache=False,
        )
