import errno
import fcntl
import os
from functools import wraps
from pathlib import Path


API_CALL_LOCK_PATH = (
    Path(__file__).resolve().parents[3]
    / "logs"
    / "api_call.lock"
)


def serialized_api_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        path = API_CALL_LOCK_PATH

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        fd = os.open(
            str(path),
            os.O_RDWR | os.O_CREAT,
            0o600,
        )

        try:
            try:
                fcntl.flock(
                    fd,
                    fcntl.LOCK_EX | fcntl.LOCK_NB,
                )
            except OSError as exc:
                if exc.errno not in (
                    errno.EAGAIN,
                    errno.EACCES,
                ):
                    raise

                raise RuntimeError(
                    "別のAPI処理が実行中です。"
                    "同時API通信を防ぐため停止します"
                ) from exc

            return function(*args, **kwargs)
        finally:
            os.close(fd)

    return wrapper
