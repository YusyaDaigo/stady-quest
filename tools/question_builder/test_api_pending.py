import json
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.question_builder.core.api_pending import (
    begin_api_request,
    finish_api_request,
)


class ApiPendingTests(unittest.TestCase):

    def test_pending_record_is_private(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pending.json"

            begin_api_request(
                model="test-model",
                path=path,
            )

            data = json.loads(
                path.read_text(encoding="utf-8")
            )

            self.assertEqual(
                set(data),
                {"startedAtUtc", "model"},
            )
            self.assertEqual(
                data["model"],
                "test-model",
            )
            self.assertEqual(
                stat.S_IMODE(path.stat().st_mode),
                0o600,
            )

    def test_existing_pending_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pending.json"

            begin_api_request(
                model="test-model",
                path=path,
            )

            with self.assertRaisesRegex(
                RuntimeError,
                "未完了",
            ):
                begin_api_request(
                    model="test-model",
                    path=path,
                )

    def test_finish_allows_next_request(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pending.json"

            begin_api_request(
                model="test-model",
                path=path,
            )

            finish_api_request(path=path)
            self.assertFalse(path.exists())

            begin_api_request(
                model="test-model",
                path=path,
            )
            self.assertTrue(path.exists())

    def test_new_process_detects_pending(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pending.json"

            begin_api_request(
                model="test-model",
                path=path,
            )

            script = """
import sys
from tools.question_builder.core.api_pending import (
    begin_api_request,
)

try:
    begin_api_request(
        model="test-model",
        path=sys.argv[1],
    )
except RuntimeError as exc:
    if "未完了" not in str(exc):
        raise
    print("BLOCKED")
else:
    print("UNEXPECTED")
"""

            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    script,
                    str(path),
                ],
                capture_output=True,
                text=True,
                timeout=10,
                check=True,
            )

            self.assertEqual(
                result.stdout.strip(),
                "BLOCKED",
            )


if __name__ == "__main__":
    unittest.main()
