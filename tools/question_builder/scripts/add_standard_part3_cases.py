import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

MANIFEST_PATH = (
    ROOT
    / "tools"
    / "question_builder"
    / "manual"
    / "practical_case_pairs.json"
)

PART3_CASE_START = 286
PART3_CASE_END = 325


def build_standard_part3_pairs():
    return [
        [first, first + 1]
        for first in range(
            PART3_CASE_START,
            PART3_CASE_END + 1,
            2,
        )
    ]


def load_manifest():
    if not MANIFEST_PATH.exists():
        return {}

    return json.loads(
        MANIFEST_PATH.read_text(
            encoding="utf-8"
        )
    )


def normalize_existing_pairs(raw_pairs):
    result = []

    for item in raw_pairs:
        if (
            isinstance(item, list)
            and len(item) == 2
        ):
            result.append([
                int(item[0]),
                int(item[1]),
            ])
            continue

        if isinstance(item, dict):
            first = (
                item.get("first")
                or item.get(
                    "first_question_no"
                )
            )
            second = (
                item.get("second")
                or item.get(
                    "second_question_no"
                )
            )

            if (
                first is not None
                and second is not None
            ):
                result.append([
                    int(first),
                    int(second),
                ])

    return result


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--exam",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
    )

    args = parser.parse_args()

    manifest = load_manifest()

    exam_key = str(args.exam)

    existing = normalize_existing_pairs(
        manifest.get(exam_key, [])
    )

    standard_pairs = (
        build_standard_part3_pairs()
    )

    existing_set = {
        tuple(pair)
        for pair in existing
    }

    additions = [
        pair
        for pair in standard_pairs
        if tuple(pair) not in existing_set
    ]

    merged = list(existing)

    for pair in additions:
        merged.append(pair)

    merged.sort(
        key=lambda pair: (
            pair[0],
            pair[1],
        )
    )

    print("==============================")
    print(
        f"STANDARD PART3 CASES: "
        f"第{args.exam}回"
    )
    print("==============================")

    print(
        "standard case groups :",
        len(standard_pairs),
    )

    print(
        "existing groups      :",
        len(existing),
    )

    print(
        "new groups           :",
        len(additions),
    )

    print()

    print(
        "standard range       : "
        "Q286-Q325"
    )

    print(
        "single range         : "
        "Q326-Q345"
    )

    print()

    for first, second in standard_pairs:
        marker = (
            "existing"
            if (
                first,
                second,
            ) in existing_set
            else "add"
        )

        print(
            f"{marker:8} "
            f"{args.exam}-"
            f"{first}-{second}"
        )

    #
    # 安全監査
    #
    if len(standard_pairs) != 20:
        raise RuntimeError(
            "標準Part3 caseが"
            "20組ではありません"
        )

    expected_numbers = list(
        range(286, 326)
    )

    actual_numbers = sorted(
        number
        for pair in standard_pairs
        for number in pair
    )

    if actual_numbers != expected_numbers:
        raise RuntimeError(
            "Q286-Q325を"
            "完全にカバーしていません"
        )

    if any(
        first >= 326
        or second >= 326
        for first, second
        in standard_pairs
    ):
        raise RuntimeError(
            "Q326以降がcaseに"
            "混入しています"
        )

    #
    # merged manifest の安全監査
    #
    invalid_single_pairs = [
        pair
        for pair in merged
        if any(
            326 <= number <= 345
            for number in pair
        )
    ]

    if invalid_single_pairs:
        raise RuntimeError(
            "Q326-Q345は単問ですが、"
            "既存manifestにcase指定があります: "
            f"{invalid_single_pairs}"
        )

    print()
    print(
        "✅ Q286-Q325 = "
        "20 case / 40 questions"
    )

    print(
        "✅ Q326-Q345 = "
        "manifest追加なし"
    )

    if args.dry_run:
        print()
        print(
            "DRY RUN: "
            "manifestは変更していません"
        )
        return

    manifest[exam_key] = merged

    MANIFEST_PATH.write_text(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print()
    print(
        "✅ manifest updated:"
    )

    print(
        MANIFEST_PATH
    )


if __name__ == "__main__":
    main()
