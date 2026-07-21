import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class OpenAITextClient:
    """
    OpenAI Responses APIを使うテキスト生成クライアント。
    """

    def __init__(
        self,
        model: str,
        *,
        max_calls_per_process: int = 1,
    ) -> None:
        if not model.strip():
            raise ValueError(
                "model must not be empty"
            )

        if max_calls_per_process < 1:
            raise ValueError(
                "max_calls_per_process must be at least 1"
            )

        self.model = model
        self.max_calls_per_process = (
            max_calls_per_process
        )
        self.call_count = 0

    def generate(
        self,
        prompt: str,
        *,
        allow_api: bool = False,
    ) -> str:
        if not isinstance(prompt, str):
            raise ValueError(
                "prompt must be a string"
            )

        if not prompt.strip():
            raise ValueError(
                "prompt must not be empty"
            )

        if not allow_api:
            raise RuntimeError(
                "OpenAI API呼び出しは無効です。"
                "実行する場合は allow_api=True を"
                "明示してください。"
            )

        if (
            self.call_count
            >= self.max_calls_per_process
        ):
            raise RuntimeError(
                "このプロセスで許可された"
                "OpenAI API呼び出し上限 "
                f"({self.max_calls_per_process}回)"
                " に達しました。"
            )

        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError(
                "OPENAI_API_KEY が設定されていません"
            )

        self.call_count += 1

        print(
            "[API CALL] "
            f"{self.call_count}/"
            f"{self.max_calls_per_process} "
            f"model={self.model}"
        )

        client = OpenAI()

        response = client.responses.create(
            model=self.model,
            input=prompt,
        )

        response_text = response.output_text

        if not response_text:
            raise ValueError(
                "OpenAI APIから空のレスポンスが"
                "返されました"
            )

        return response_text
