import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

from tools.question_builder.core.api_usage import DEFAULT_LOG


JST = timezone(timedelta(hours=9))

MONTHLY_BUDGET_JPY = Decimal("5000")
WARNING_JPY = Decimal("4000")

ESTIMATE_YEN_PER_USD = Decimal("200")

TRIAL_START = datetime(
    2026, 10, 13, tzinfo=JST
)


def budget_period(now=None):
    if now is None:
        now = datetime.now(JST)

    if now.tzinfo is None:
        raise ValueError("Timezone required")

    now = now.astimezone(JST)

    start = now.replace(
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    if start < TRIAL_START:
        start = TRIAL_START

    year = now.year
    month = now.month

    if month == 12:
        end = datetime(
            year + 1, 1, 1, tzinfo=JST
        )
    else:
        end = datetime(
            year, month + 1, 1, tzinfo=JST
        )

    return start, end


def inspect_api_budget(
    *,
    log_path=None,
    now=None,
    next_call_allowance_jpy=100,
):
    path = (
        Path(log_path)
        if log_path is not None
        else DEFAULT_LOG
    )

    start, end = budget_period(now)

    spent_usd = Decimal("0")
    unknown_count = 0
    record_count = 0

    if path.exists():
        with path.open(
            "r", encoding="utf-8"
        ) as handle:
            for number, line in enumerate(
                handle, 1
            ):
                if not line.strip():
                    continue

                try:
                    record = json.loads(line)

                    timestamp = datetime.fromisoformat(
                        record["timestampUtc"].replace(
                            "Z", "+00:00"
                        )
                    )

                    if timestamp.tzinfo is None:
                        raise ValueError(
                            "Naive timestamp"
                        )

                except (
                    ValueError,
                    TypeError,
                    KeyError,
                ) as exc:
                    raise ValueError(
                        "Invalid budget log "
                        f"at line {number}"
                    ) from exc

                timestamp = timestamp.astimezone(JST)

                if not start <= timestamp < end:
                    continue

                record_count += 1

                cost = record.get(
                    "estimatedCostUsd"
                )

                if cost is None:
                    unknown_count += 1
                    continue

                try:
                    amount = Decimal(str(cost))
                except InvalidOperation as exc:
                    raise ValueError(
                        "Invalid recorded cost"
                    ) from exc

                if (
                    not amount.is_finite()
                    or amount < 0
                ):
                    raise ValueError(
                        "Invalid recorded cost"
                    )

                spent_usd += amount

    spent_jpy = (
        spent_usd * ESTIMATE_YEN_PER_USD
    )

    allowance = Decimal(
        str(next_call_allowance_jpy)
    )

    if (
        not allowance.is_finite()
        or allowance < 0
    ):
        raise ValueError(
            "Invalid next-call allowance"
        )

    remaining = (
        MONTHLY_BUDGET_JPY - spent_jpy
    )

    allowed = (
        unknown_count == 0
        and spent_jpy + allowance
        <= MONTHLY_BUDGET_JPY
    )

    return {
        "periodStartJst": start.isoformat(),
        "periodEndJst": end.isoformat(),
        "monthlyBudgetJpy": float(
            MONTHLY_BUDGET_JPY
        ),
        "estimatedSpentJpy": float(
            spent_jpy
        ),
        "remainingJpy": float(remaining),
        "warning": (
            spent_jpy >= WARNING_JPY
        ),
        "unknownRecords": unknown_count,
        "recordCount": record_count,
        "allowed": allowed,
    }
