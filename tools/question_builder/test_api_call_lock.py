import fcntl
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.question_builder.core.api_call_lock import (
    serialized_api_call,
)
from tools.question_builder.core.ai_client import (
    OpenAITextClient,
)


class ApiCallLockTests(unittest.TestCase):

    def test_locked_request_does_not_start_sdk(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "api_call.lock"

            fd = os.open(
                str(path),
                os.O_RDWR | os.O_CREAT,
                0o600,
            )

            fcntl.flock(fd, fcntl.LOCK_EX)

            try:
                with (
                    patch(
                        "tools.question_builder.core."
                        "api_call_lock.API_CALL_LOCK_PATH",
                        path,
                    ),
                    patch(
                        "tools.question_builder.core."
                        "ai_client.OpenAI",
                    ) as sdk,
                ):
                    client = OpenAITextClient(
                        model="test-model",
                    )

                    with self.assertRaisesRegex(
                        RuntimeError,
                        "別のAPI処理",
                    ):
                        client.generate(
                            "test prompt",
                            allow_api=True,
                        )

                    sdk.assert_not_called()
                    self.assertEqual(
                        client.call_count,
                        0,
                    )
            finally:
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)

    def test_lock_released_after_exception(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "api_call.lock"

            @serialized_api_call
            def work(*, fail=False):
                if fail:
                    raise ValueError("test failure")
                return "OK"

            with patch(
                "tools.question_builder.core."
                "api_call_lock.API_CALL_LOCK_PATH",
                path,
            ):
                with self.assertRaises(ValueError):
                    work(fail=True)

                self.assertEqual(
                    work(),
                    "OK",
                )

    def test_second_process_is_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "api_call.lock"

            fd = os.open(
                str(path),
                os.O_RDWR | os.O_CREAT,
                0o600,
            )

            fcntl.flock(fd, fcntl.LOCK_EX)

            script = """
import errno
import fcntl
import os
import sys

fd = os.open(sys.argv[1], os.O_RDWR)

try:
    try:
        fcntl.flock(
            fd,
            fcntl.LOCK_EX | fcntl.LOCK_NB,
        )
    except OSError as exc:
        if exc.errno in (
            errno.EAGAIN,
            errno.EACCES,
        ):
            print("BLOCKED")
        else:
            raise
    else:
        print("UNEXPECTEDLY_ACQUIRED")
finally:
    os.close(fd)
"""

            try:
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
            finally:
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)


if __name__ == "__main__":
    unittest.main()
