import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from openai import OpenAI

from tools.question_builder.similar_question_generator import (
    build_similar_question_prompt,
)
from tools.question_builder.similar_question_response_parser import (
    parse_similar_question_response,
)


load_dotenv()


SIMILAR_QUESTION_MODEL = "gpt-5.5"

SIMILAR_QUESTION_CACHE_DIR = Path(
    "generated_questions/cache/similar_questions"
)

_API_CALL_COUNT = 0
MAX_API_CALLS_PER_PROCESS = 1


def _build_cache_key(
    source_question: Dict[str, Any],
    prompt: str,
    model: str,
) -> str:
    """
    元問題・プロンプト・モデルから
    一意のキャッシュキーを作る。
    """

    payload = {
        "sourceQuestion": source_question,
        "prompt": prompt,
        "model": model,
    }

    serialized = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def _build_cache_path(
    cache_key: str,
) -> Path:
    """
    キャッシュファイルの保存先を返す。
    """

    return (
        SIMILAR_QUESTION_CACHE_DIR
        / f"{cache_key}.json"
    )


def _load_cached_question(
    cache_path: Path,
) -> Dict[str, Any]:
    """
    保存済みキャッシュを読み込む。
    """

    with cache_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            f"Invalid similar question cache: {cache_path}"
        )

    return data


def _save_cached_question(
    cache_path: Path,
    question: Dict[str, Any],
) -> None:
    """
    生成済み類題をキャッシュへ保存する。
    """

    cache_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with cache_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            question,
            file,
            ensure_ascii=False,
            indent=2,
        )


def generate_similar_question(
    source_question: Dict[str, Any],
    *,
    allow_api: bool = False,
    use_cache: bool = True,
) -> Dict[str, Any]:
    """
    元問題1問から類題を1問生成する。

    安全仕様:
    - キャッシュがあればAPIを呼ばず再利用する
    - allow_api=False がデフォルト
    - allow_api=True のときだけOpenAI APIを呼ぶ
    """

    global _API_CALL_COUNT

    prompt = build_similar_question_prompt(
        source_question
    )

    cache_key = _build_cache_key(
        source_question=source_question,
        prompt=prompt,
        model=SIMILAR_QUESTION_MODEL,
    )

    cache_path = _build_cache_path(
        cache_key
    )

    if (
        use_cache
        and cache_path.exists()
    ):
        print(
            "[CACHE HIT] "
            f"{cache_path}"
        )

        return _load_cached_question(
            cache_path
        )

    if not allow_api:
        raise RuntimeError(
            "OpenAI API呼び出しは無効です。"
            "APIを1回だけ実行する場合は "
            "allow_api=True を明示してください。"
        )

    if _API_CALL_COUNT >= MAX_API_CALLS_PER_PROCESS:
        raise RuntimeError(
            "このプロセスで許可されたOpenAI API呼び出し上限 "
            f"({MAX_API_CALLS_PER_PROCESS}回) に達しました。"
        )

    if not os.getenv(
        "OPENAI_API_KEY"
    ):
        raise RuntimeError(
            "OPENAI_API_KEY が設定されていません"
        )

    _API_CALL_COUNT += 1

    print(
        "[API CALL] "
        f"{_API_CALL_COUNT}/{MAX_API_CALLS_PER_PROCESS} "
        f"model={SIMILAR_QUESTION_MODEL}"
    )

    client = OpenAI()

    response = client.responses.create(
        model=SIMILAR_QUESTION_MODEL,
        input=prompt,
    )

    response_text = (
        response.output_text
    )

    if not response_text:
        raise ValueError(
            "OpenAI APIから空のレスポンスが返されました"
        )

    generated_question = (
        parse_similar_question_response(
            response_text
        )
    )

    if use_cache:
        _save_cached_question(
            cache_path=cache_path,
            question=generated_question,
        )

        print(
            "[CACHE SAVED] "
            f"{cache_path}"
        )

    return generated_question
