import json
import os
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path


PRICES = {
    "gpt-6-luna": ("0.10", "0.01", "0.50"),
    "gpt-5.4-mini": ("0.75", "0.075", "4.50"),
    "gpt-5.5": ("5.00", "0.50", "30.00"),
}

PRICING_DATE = "2026-10-13"

DEFAULT_LOG = (
    Path(__file__).resolve().parents[3]
    / "logs"
    / "api_usage.jsonl"
)


def _field(value, name):
    if isinstance(value, dict):
        return value.get(name)
    return getattr(value, name, None)


def _valid_tokens(value):
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= 0
    )


def build_usage_record(
    *,
    model,
    usage=None,
    status="completed",
):
    if status not in ("completed", "request_failed"):
        raise ValueError("Invalid API status")

    input_tokens = _field(usage, "input_tokens")
    output_tokens = _field(usage, "output_tokens")

    details = _field(
        usage, "input_tokens_details"
    )

    cached_tokens = _field(
        details, "cached_tokens"
    )

    estimate = None
    estimate_status = "unavailable"

    if (
        model in PRICES
        and _valid_tokens(input_tokens)
        and _valid_tokens(output_tokens)
        and _valid_tokens(cached_tokens)
        and cached_tokens <= input_tokens
        and input_tokens < 272000
    ):
        input_rate, cached_rate, output_rate = (
            map(Decimal, PRICES[model])
        )

        amount = (
            Decimal(input_tokens - cached_tokens)
            * input_rate
            + Decimal(cached_tokens)
            * cached_rate
            + Decimal(output_tokens)
            * output_rate
        ) / Decimal(1000000)

        estimate = float(
            amount.quantize(
                Decimal("0.00000001")
            )
        )

        estimate_status = (
            "standard_short_text_estimate"
        )

    return {
        "timestampUtc": datetime.now(
            timezone.utc
        ).isoformat(),
        "operation": "text_generation",
        "model": model,
        "status": status,
        "inputTokens": (
            input_tokens
            if _valid_tokens(input_tokens)
            else None
        ),
        "outputTokens": (
            output_tokens
            if _valid_tokens(output_tokens)
            else None
        ),
        "cachedInputTokens": (
            cached_tokens
            if _valid_tokens(cached_tokens)
            else None
        ),
        "estimatedCostUsd": estimate,
        "estimateStatus": estimate_status,
        "pricingDate": PRICING_DATE,
    }


def record_api_usage(
    *,
    model,
    usage=None,
    status="completed",
    log_path=None,
):
    record = build_usage_record(
        model=model,
        usage=usage,
        status=status,
    )

    path = (
        Path(log_path)
        if log_path is not None
        else DEFAULT_LOG
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    data = (
        json.dumps(
            record,
            ensure_ascii=False,
        ) + "\n"
    ).encode("utf-8")

    fd = os.open(
        str(path),
        os.O_WRONLY | os.O_CREAT | os.O_APPEND,
        0o600,
    )

    try:
        os.write(fd, data)
    finally:
        os.close(fd)

    return record
