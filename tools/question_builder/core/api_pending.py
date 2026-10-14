import json
import os
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_PENDING_PATH = (
    Path(__file__).resolve().parents[3]
    / "logs"
    / "api_pending.json"
)


def begin_api_request(*, model, path=None):
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Invalid model")

    target = (
        Path(path)
        if path is not None
        else DEFAULT_PENDING_PATH
    )

    target.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "startedAtUtc": datetime.now(
            timezone.utc
        ).isoformat(),
        "model": model,
    }

    try:
        fd = os.open(
            str(target),
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
    except FileExistsError as exc:
        raise RuntimeError(
            "未完了のAPI呼び出しが残っています。"
            "料金履歴を確認するまで追加通信を停止します"
        ) from exc

    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(record, handle, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())

    return target


def finish_api_request(*, path=None):
    target = (
        Path(path)
        if path is not None
        else DEFAULT_PENDING_PATH
    )

    target.unlink()
