import json
import tempfile
import unittest
from pathlib import Path

from tools.question_builder.core.api_usage import (
    build_usage_record,
    record_api_usage,
)


class ApiUsageTests(unittest.TestCase):
    def test_estimate_with_cached_tokens(self):
        record = build_usage_record(
            model="gpt-6-luna",
            usage={
                "input_tokens": 1000,
                "output_tokens": 200,
                "input_tokens_details": {
                    "cached_tokens": 100,
                },
            },
        )

        self.assertAlmostEqual(
            record["estimatedCostUsd"],
            0.000191,
        )

        self.assertEqual(
            record["status"],
            "completed",
        )

    def test_missing_usage_is_unknown(self):
        record = build_usage_record(
            model="gpt-6-luna",
            usage=None,
            status="request_failed",
        )

        self.assertIsNone(
            record["estimatedCostUsd"]
        )

        self.assertIsNone(
            record["inputTokens"]
        )

    def test_unknown_model_is_unknown(self):
        record = build_usage_record(
            model="unknown-model",
            usage={
                "input_tokens": 100,
                "output_tokens": 50,
                "input_tokens_details": {
                    "cached_tokens": 0,
                },
            },
        )

        self.assertIsNone(
            record["estimatedCostUsd"]
        )

    def test_private_local_jsonl(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "usage.jsonl"

            record_api_usage(
                model="gpt-6-luna",
                usage={
                    "input_tokens": 100,
                    "output_tokens": 50,
                    "input_tokens_details": {
                        "cached_tokens": 0,
                    },
                },
                log_path=path,
            )

            records = [
                json.loads(line)
                for line in path.read_text(
                    encoding="utf-8"
                ).splitlines()
            ]

            self.assertEqual(len(records), 1)

            self.assertEqual(
                records[0]["model"],
                "gpt-6-luna",
            )

            self.assertNotIn(
                "prompt",
                records[0],
            )



class TextClientUsageIntegrationTests(unittest.TestCase):

    def setUp(self):
        from unittest.mock import patch

        self._guard_patch = patch(
            "tools.question_builder.api_policy._usage_log_failed",
            False,
        )
        self._guard_patch.start()
        self.addCleanup(self._guard_patch.stop)

    def test_success_logs_tokens_and_cost(self):
        import os
        from unittest.mock import patch
        from types import SimpleNamespace
        from tools.question_builder.core.ai_client import (
            OpenAITextClient,
        )

        with tempfile.TemporaryDirectory() as temp:
            log = Path(temp) / "usage.jsonl"

            response = SimpleNamespace(
                output_text="TEST OUTPUT",
                usage={
                    "input_tokens": 1000,
                    "output_tokens": 200,
                    "input_tokens_details": {
                        "cached_tokens": 100,
                    },
                },
            )

            with (
                patch.dict(
                    os.environ,
                    {
                        "STUDY_QUEST_ALLOW_API": "1",
                        "OPENAI_API_KEY": "dummy",
                    },
                    clear=True,
                ),
                patch(
                    "tools.question_builder.core."
                    "api_usage.DEFAULT_LOG",
                    log,
                ),
                patch(
                    "tools.question_builder.core."
                    "ai_client.OpenAI"
                ) as sdk,
            ):
                sdk.return_value.responses.create.return_value = (
                    response
                )

                result = OpenAITextClient(
                    model="gpt-6-luna"
                ).generate(
                    "test prompt",
                    allow_api=True,
                )

                self.assertEqual(result, "TEST OUTPUT")
                sdk.return_value.responses.create.assert_called_once()

            entry = json.loads(
                log.read_text(encoding="utf-8").strip()
            )

            self.assertEqual(entry["status"], "completed")
            self.assertEqual(entry["inputTokens"], 1000)
            self.assertEqual(entry["outputTokens"], 200)
            self.assertEqual(entry["cachedInputTokens"], 100)
            self.assertAlmostEqual(
                entry["estimatedCostUsd"],
                0.000191,
            )
            self.assertNotIn("test prompt", str(entry))

    def test_sdk_failure_logs_unknown_cost(self):
        import os
        from unittest.mock import patch
        from tools.question_builder.core.ai_client import (
            OpenAITextClient,
        )

        with tempfile.TemporaryDirectory() as temp:
            log = Path(temp) / "usage.jsonl"

            with (
                patch.dict(
                    os.environ,
                    {
                        "STUDY_QUEST_ALLOW_API": "1",
                        "OPENAI_API_KEY": "dummy",
                    },
                    clear=True,
                ),
                patch(
                    "tools.question_builder.core."
                    "api_usage.DEFAULT_LOG",
                    log,
                ),
                patch(
                    "tools.question_builder.core."
                    "ai_client.OpenAI"
                ) as sdk,
            ):
                sdk.return_value.responses.create.side_effect = (
                    RuntimeError("simulated API failure")
                )

                with self.assertRaisesRegex(
                    RuntimeError,
                    "simulated API failure",
                ):
                    OpenAITextClient(
                        model="gpt-6-luna"
                    ).generate(
                        "test prompt",
                        allow_api=True,
                    )

            entry = json.loads(
                log.read_text(encoding="utf-8").strip()
            )

            self.assertEqual(
                entry["status"],
                "request_failed",
            )
            self.assertIsNone(
                entry["estimatedCostUsd"]
            )

    def test_default_off_creates_no_log(self):
        import os
        from unittest.mock import patch
        from tools.question_builder.core.ai_client import (
            OpenAITextClient,
        )

        with tempfile.TemporaryDirectory() as temp:
            log = Path(temp) / "usage.jsonl"

            with (
                patch.dict(
                    os.environ,
                    {"OPENAI_API_KEY": "dummy"},
                    clear=True,
                ),
                patch(
                    "tools.question_builder.core."
                    "api_usage.DEFAULT_LOG",
                    log,
                ),
                patch(
                    "tools.question_builder.core."
                    "ai_client.OpenAI"
                ) as sdk,
            ):
                with self.assertRaises(RuntimeError):
                    OpenAITextClient(
                        model="gpt-6-luna"
                    ).generate(
                        "test prompt",
                        allow_api=True,
                    )

                sdk.assert_not_called()
                self.assertFalse(log.exists())

    def test_logging_failure_preserves_output(self):
        import os
        from types import SimpleNamespace
        from unittest.mock import patch
        from tools.question_builder.core.ai_client import (
            OpenAITextClient,
        )

        with (
            patch.dict(
                os.environ,
                {
                    "STUDY_QUEST_ALLOW_API": "1",
                    "OPENAI_API_KEY": "dummy",
                },
                clear=True,
            ),
            patch(
                "tools.question_builder.core."
                "ai_client.OpenAI"
            ) as sdk,
            patch(
                "tools.question_builder.core."
                "ai_client.record_api_usage",
                side_effect=OSError("simulated disk error"),
            ),
        ):
            sdk.return_value.responses.create.return_value = (
                SimpleNamespace(
                    output_text="VALID RESPONSE",
                    usage=None,
                )
            )

            result = OpenAITextClient(
                model="gpt-6-luna"
            ).generate(
                "test prompt",
                allow_api=True,
            )

            self.assertEqual(
                result,
                "VALID RESPONSE",
            )

            with self.assertRaisesRegex(
                RuntimeError,
                "ログ保存に失敗",
            ):
                OpenAITextClient(
                    model="gpt-6-luna",
                ).generate(
                    "second prompt",
                    allow_api=True,
                )

            sdk.return_value.responses.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
