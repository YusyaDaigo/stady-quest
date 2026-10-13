import os


def require_api_permission() -> None:
    """API利用は明示的に許可された場合だけ認める。"""

    if os.getenv("STUDY_QUEST_NO_API") == "1":
        raise RuntimeError(
            "STUDY_QUEST_NO_API=1 のため"
            "OpenAI APIを呼びません"
        )

    if os.getenv("STUDY_QUEST_ALLOW_API") != "1":
        raise RuntimeError(
            "OpenAI APIは標準で無効です。"
            "実行には STUDY_QUEST_ALLOW_API=1 "
            "が必要です"
        )
