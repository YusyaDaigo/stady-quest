import os

from dotenv import load_dotenv
from openai import OpenAI

from tools.question_builder.api_policy import require_api_permission
from tools.question_builder.core.api_usage import record_api_usage


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

    def _record_usage_safely(
        self,
        *,
        usage,
        status: str,
    ) -> None:
        try:
            record_api_usage(
                model=self.model,
                usage=usage,
                status=status,
            )
        except Exception as exc:
            print(
                "[API USAGE WARNING] "
                "ログ保存に失敗: "
                f"{type(exc).__name__}"
            )

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

        if os.getenv("STUDY_QUEST_NO_API") == "1":
            raise RuntimeError(
                "STUDY_QUEST_NO_API=1 のため"
                "OpenAI APIを呼びません"
            )

        require_api_permission()

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

        response = None

        try:
            client = OpenAI()
            response = client.responses.create(
                model=self.model,
                input=prompt,
            )
            response_text = response.output_text
        except Exception:
            self._record_usage_safely(
                usage=getattr(response, "usage", None),
                status="request_failed",
            )
            raise

        self._record_usage_safely(
            usage=getattr(response, "usage", None),
            status=(
                "completed"
                if response_text
                else "request_failed"
            ),
        )

        if not response_text:
            raise ValueError(
                "OpenAI APIから空のレスポンスが"
                "返されました"
            )

        return response_text
