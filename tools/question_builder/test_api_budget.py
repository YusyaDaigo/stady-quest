import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from tools.question_builder.core.api_budget import (
    JST,
    inspect_api_budget,
)


class BudgetTests(unittest.TestCase):

    def test_empty_budget(self):
        with tempfile.TemporaryDirectory() as temp:
            result = inspect_api_budget(
                log_path=Path(temp) / "missing.jsonl",
                now=datetime(
                    2026, 10, 13, 12,
                    tzinfo=JST,
                ),
            )

            self.assertTrue(result["allowed"])
            self.assertEqual(
                result["remainingJpy"],
                5000,
            )

    def test_earlier_spending_excluded(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "usage.jsonl"

            records = [
                {
                    "timestampUtc":
                        "2026-10-12T00:00:00+00:00",
                    "estimatedCostUsd": 100,
                },
                {
                    "timestampUtc":
                        "2026-10-13T06:00:00+00:00",
                    "estimatedCostUsd": 1,
                },
            ]

            path.write_text(
                "".join(
                    json.dumps(record) + "\n"
                    for record in records
                ),
                encoding="utf-8",
            )

            result = inspect_api_budget(
                log_path=path,
                now=datetime(
                    2026, 10, 14,
                    tzinfo=JST,
                ),
            )

            self.assertEqual(
                result["estimatedSpentJpy"],
                200,
            )

    def test_near_limit_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "usage.jsonl"

            path.write_text(
                json.dumps({
                    "timestampUtc":
                        "2026-10-15T00:00:00+00:00",
                    "estimatedCostUsd": 24.5,
                }) + "\n",
                encoding="utf-8",
            )

            result = inspect_api_budget(
                log_path=path,
                now=datetime(
                    2026, 10, 16,
                    tzinfo=JST,
                ),
                next_call_allowance_jpy=200,
            )

            self.assertFalse(result["allowed"])
            self.assertTrue(result["warning"])

    def test_unknown_cost_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "usage.jsonl"

            path.write_text(
                json.dumps({
                    "timestampUtc":
                        "2026-10-15T00:00:00+00:00",
                    "estimatedCostUsd": None,
                }) + "\n",
                encoding="utf-8",
            )

            result = inspect_api_budget(
                log_path=path,
                now=datetime(
                    2026, 10, 16,
                    tzinfo=JST,
                ),
            )

            self.assertFalse(result["allowed"])
            self.assertEqual(
                result["unknownRecords"],
                1,
            )

    def test_new_month_resets(self):
        with tempfile.TemporaryDirectory() as temp:
            result = inspect_api_budget(
                log_path=Path(temp) / "missing.jsonl",
                now=datetime(
                    2026, 11, 1,
                    tzinfo=JST,
                ),
            )

            self.assertTrue(result["allowed"])
            self.assertEqual(
                result["remainingJpy"],
                5000,
            )


if __name__ == "__main__":
    unittest.main()
