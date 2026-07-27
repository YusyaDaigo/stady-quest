from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Union

from tools.question_builder.core.ai_client import (
    OpenAITextClient,
)
from tools.question_builder.core.cache import (
    JsonCache,
)

from tools.question_builder.templates.engine import (
    compose_prompt,
)


GeneratedData = Union[
    dict[str, Any],
    list[dict[str, Any]],
]


class BaseGenerator(ABC):
    """
    AI問題生成処理の共通基底クラス。

    処理順:
    1. Prompt生成
    2. キャッシュ確認
    3. キャッシュ検証
    4. OpenAI API呼び出し
    5. レスポンス解析
    6. キャッシュ保存
    """

    template_path: Path
    partial_paths: tuple[Path, ...] = ()

    def __init__(
        self,
        *,
        model: str,
        cache_dir: Path,
        max_api_calls: int = 1,
    ) -> None:
        self.model = model

        self.cache = JsonCache(
            cache_dir=cache_dir
        )

        self.ai_client = OpenAITextClient(
            model=model,
            max_calls_per_process=max_api_calls,
        )

    @abstractmethod
    def build_prompt_variables(
        self,
        input_data: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Prompt Engineへ渡すテンプレート変数を構築する。
        """
        raise NotImplementedError

    @abstractmethod
    def parse_response(
        self,
        response_text: str,
        input_data: dict[str, Any],
    ) -> GeneratedData:
        """
        AIレスポンスを検証済みデータへ変換する。
        """

    def build_cache_payload(
        self,
        input_data: dict[str, Any],
        prompt: str,
    ) -> dict[str, Any]:
        return {
            "inputData": input_data,
            "prompt": prompt,
            "model": self.model,
            "generator": (
                self.__class__.__name__
            ),
        }

    def validate_cached_result(
        self,
        cached: GeneratedData,
        input_data: dict[str, Any],
    ) -> GeneratedData:
        """
        サブクラス固有のキャッシュ検証フック。
        """

        return cached

    def generate(
        self,
        input_data: dict[str, Any],
        *,
        allow_api: bool = False,
        use_cache: bool = True,
    ) -> GeneratedData:
        if not isinstance(input_data, dict):
            raise ValueError(
                "input_data must be a dictionary"
            )

        variables = self.build_prompt_variables(
            input_data
        )

        prompt = compose_prompt(
            template_path=self.template_path,
            partial_paths=self.partial_paths,
            variables=variables,
        )

        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError(
                "generated prompt must be a non-empty string"
            )

        cache_payload = (
            self.build_cache_payload(
                input_data=input_data,
                prompt=prompt,
            )
        )

        cache_key = self.cache.build_key(
            cache_payload
        )

        if use_cache:
            cached = self.cache.load(
                cache_key
            )

            if cached is not None:
                validated_cached = (
                    self.validate_cached_result(
                        cached=cached,
                        input_data=input_data,
                    )
                )

                print(
                    "[CACHE HIT] "
                    f"{self.cache.build_path(cache_key)}"
                )

                return validated_cached

        response_text = (
            self.ai_client.generate(
                prompt=prompt,
                allow_api=allow_api,
            )
        )

        generated = self.parse_response(
            response_text=response_text,
            input_data=input_data,
        )

        if use_cache:
            cache_path = self.cache.save(
                cache_key=cache_key,
                data=generated,
            )

            print(
                f"[CACHE SAVED] {cache_path}"
            )

        return generated
