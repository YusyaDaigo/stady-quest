import os



_usage_log_failed = False


def mark_api_usage_logging_failed() -> None:
    global _usage_log_failed
    _usage_log_failed = True


def require_api_permission(*, usage_tracked=False) -> None:
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

    if _usage_log_failed:
        raise RuntimeError(
            "API利用履歴のログ保存に失敗したため、"
            "このプロセスでの追加API通信を停止します"
        )

    if not usage_tracked:
        raise RuntimeError(
            "このAPI経路は使用料金の記録が未対応です。"
            "予算管理が完成するまでAPI利用を停止します"
        )

    from tools.question_builder.core.api_budget import inspect_api_budget

    budget = inspect_api_budget(
        next_call_allowance_usd=2,
    )

    if not budget["allowed"]:
        raise RuntimeError(
            "API予算チェックにより実行を停止しました。"
            f"推定残額: ${budget['remainingUsd']:.2f}、"
            f"料金不明の記録: {budget['unknownRecords']}件"
        )
