from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class JsonCache:
    """
    JSON形式の生成結果を保存・再利用する共通キャッシュ。

    JSONルートはobjectまたはarrayを許可する。
    """

    def __init__(
        self,
        cache_dir: Path,
    ) -> None:
        self.cache_dir = Path(cache_dir)

    def build_key(
        self,
        payload: dict[str, Any],
    ) -> str:
        if not isinstance(payload, dict):
            raise ValueError(
                "cache key payload must be a dictionary"
            )

        serialized = json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

        return hashlib.sha256(
            serialized.encode("utf-8")
        ).hexdigest()

    def build_path(
        self,
        cache_key: str,
    ) -> Path:
        return self.cache_dir / f"{cache_key}.json"

    def load(
        self,
        cache_key: str,
    ) -> dict[str, Any] | list[Any] | None:
        cache_path = self.build_path(
            cache_key
        )

        if not cache_path.exists():
            return None

        with cache_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        if not isinstance(data, (dict, list)):
            raise ValueError(
                "Invalid JSON cache root. "
                "Expected object or array: "
                f"{cache_path}"
            )

        return data

    def save(
        self,
        cache_key: str,
        data: dict[str, Any] | list[Any],
    ) -> Path:
        if not isinstance(data, (dict, list)):
            raise ValueError(
                "cache data must be a dictionary or list"
            )

        cache_path = self.build_path(
            cache_key
        )

        cache_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with cache_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=2,
            )

        return cache_path
