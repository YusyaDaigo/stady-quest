import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path


CASE_MANIFEST_PATH = Path(
    "tools/question_builder/manual/"
    "practical_case_pairs.json"
)

CASE_CACHE_BASE = Path(
    "tools/question_builder/cache/pharmacy/"
    "practical/cases"
)

REBUILD_SCRIPT = Path(
    "tools/question_builder/scripts/"
    "rebuild_practical_case_cache.py"
)

GENERATED_QUESTION_BASE = Path(
    "src/exams/pharmacy/questions"
)


def load_case_pairs(
    exam_number: int,
) -> list:
    if not CASE_MANIFEST_PATH.exists():
        raise FileNotFoundError(
            "case manifestがありません: "
            f"{CASE_MANIFEST_PATH}"
        )

    data = json.loads(
        CASE_MANIFEST_PATH.read_text(
            encoding="utf-8"
        )
    )

    raw_pairs = data.get(
        str(exam_number)
    )

    if not isinstance(
        raw_pairs,
        list,
    ):
        raise ValueError(
            "case manifestに年度がありません: "
            f"{exam_number}"
        )

    pairs = []

    for raw_pair in raw_pairs:
        if (
            not isinstance(
                raw_pair,
                list,
            )
            or len(raw_pair) != 2
        ):
            raise ValueError(
                "不正なcase pair: "
                f"{raw_pair}"
            )

        first_no = int(
            raw_pair[0]
        )
        second_no = int(
            raw_pair[1]
        )

        if second_no != first_no + 1:
            raise ValueError(
                "連番ではないcase pair: "
                f"{raw_pair}"
            )

        pairs.append(
            (
                first_no,
                second_no,
            )
        )

    return pairs


def load_generated_question_numbers(
    exam_number: int,
) -> set:
    path = (
        GENERATED_QUESTION_BASE
        / f"practical_{exam_number}.js"
    )

    if not path.exists():
        raise FileNotFoundError(
            "生成済み実践問題がありません: "
            f"{path}"
        )

    text = path.read_text(
        encoding="utf-8"
    )

    return {
        int(number)
        for number in re.findall(
            r"sourceNumber:\s*(\d+)",
            text,
        )
    }


def is_valid_case_cache(
    path: Path,
    exam_number: int,
    first_no: int,
    second_no: int,
) -> bool:
    if not path.exists():
        return False

    try:
        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )
    except Exception:
        return False

    expected_case_id = (
        f"{exam_number}-"
        f"{first_no}-"
        f"{second_no}"
    )

    case_id = data.get(
        "case_id"
    )

    case_context = data.get(
        "case_context",
        "",
    )

    questions = data.get(
        "questions"
    )

    if (
        case_id != expected_case_id
        or not isinstance(
            case_context,
            str,
        )
        or not case_context.strip()
        or not isinstance(
            questions,
            list,
        )
        or len(questions) != 2
    ):
        return False

    invalid_phrases = [
        "画像内に2問共通の症例",
        "確認できない",
        "提示されていない",
    ]

    if any(
        phrase in case_context
        for phrase in invalid_phrases
    ):
        return False

    actual_numbers = []

    for question in questions:
        if not isinstance(
            question,
            dict,
        ):
            return False

        try:
            question_no = int(
                question.get(
                    "question_no"
                )
            )
        except (
            TypeError,
            ValueError,
        ):
            return False

        question_text = question.get(
            "question",
            "",
        )

        choices = question.get(
            "choices",
            [],
        )

        if (
            not isinstance(
                question_text,
                str,
            )
            or not question_text.strip()
            or not isinstance(
                choices,
                list,
            )
            or len(choices) < 2
        ):
            return False

        actual_numbers.append(
            question_no
        )

    return sorted(
        actual_numbers
    ) == [
        first_no,
        second_no,
    ]


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "不足している実践問題case cacheを"
            "manifestから再構築する"
        )
    )

    parser.add_argument(
        "--exam",
        type=int,
        required=True,
        help="試験回数",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "APIを呼ばず、"
            "再構築対象だけ表示する"
        ),
    )

    return parser.parse_args()


def main():
    args = parse_args()

    exam_number = args.exam

    target_pairs = load_case_pairs(
        exam_number
    )

    generated_numbers = (
        load_generated_question_numbers(
            exam_number
        )
    )

    case_cache_root = (
        CASE_CACHE_BASE
        / str(exam_number)
    )

    if not args.dry_run:
        case_cache_root.mkdir(
            parents=True,
            exist_ok=True,
        )

    success = []
    skipped_valid = []
    skipped_incomplete_source = []
    rebuild_targets = []
    failed = []

    total = len(
        target_pairs
    )

    print(
        "=============================="
    )
    print(
        "PRACTICAL CASE BATCH REBUILD"
    )
    print(
        "=============================="
    )
    print(
        f"試験回数    : {exam_number}"
    )
    print(
        f"manifest数  : {total}"
    )
    print(
        f"dry-run     : {args.dry_run}"
    )
    print(
        "=============================="
    )

    for (
        first_no,
        second_no,
    ) in target_pairs:
        case_name = (
            f"{first_no}-{second_no}"
        )

        cache_path = (
            case_cache_root
            / f"{case_name}.json"
        )

        missing_source_numbers = [
            number
            for number in (
                first_no,
                second_no,
            )
            if number
            not in generated_numbers
        ]

        if missing_source_numbers:
            skipped_incomplete_source.append(
                (
                    case_name,
                    missing_source_numbers,
                )
            )
            continue

        if is_valid_case_cache(
            cache_path,
            exam_number,
            first_no,
            second_no,
        ):
            skipped_valid.append(
                case_name
            )
            continue

        rebuild_targets.append(
            (
                first_no,
                second_no,
            )
        )

    print()
    print(
        "===== PLAN ====="
    )
    print(
        "完全cache済み       : "
        f"{len(skipped_valid)}"
    )
    print(
        "再構築対象           : "
        f"{len(rebuild_targets)}"
    )
    print(
        "source不足でスキップ : "
        f"{len(skipped_incomplete_source)}"
    )

    if rebuild_targets:
        print()
        print(
            "===== REBUILD TARGETS ====="
        )

        for (
            first_no,
            second_no,
        ) in rebuild_targets:
            print(
                f"  {first_no}-{second_no}"
            )

    if skipped_incomplete_source:
        print()
        print(
            "===== INCOMPLETE SOURCE ====="
        )

        for (
            case_name,
            missing_numbers,
        ) in skipped_incomplete_source:
            print(
                f"  {case_name}: "
                "missing "
                + ", ".join(
                    f"Q{number}"
                    for number
                    in missing_numbers
                )
            )

    if args.dry_run:
        print()
        print(
            "===== DRY RUN COMPLETE ====="
        )
        print(
            "APIは呼び出していません。"
        )
        return

    rebuild_total = len(
        rebuild_targets
    )

    for index, (
        first_no,
        second_no,
    ) in enumerate(
        rebuild_targets,
        start=1,
    ):
        case_name = (
            f"{first_no}-{second_no}"
        )

        cache_path = (
            case_cache_root
            / f"{case_name}.json"
        )

        print()
        print(
            f"[{index}/{rebuild_total}] "
            f"CASE {case_name}"
        )

        command = [
            sys.executable,
            str(REBUILD_SCRIPT),
            "--exam",
            str(exam_number),
            "--first",
            str(first_no),
            "--second",
            str(second_no),
            "--force",
        ]

        try:
            result = subprocess.run(
                command,
                check=False,
            )

            if (
                result.returncode == 0
                and is_valid_case_cache(
                    cache_path,
                    exam_number,
                    first_no,
                    second_no,
                )
            ):
                print(
                    f"✅ CASE {case_name} 完了"
                )

                success.append(
                    case_name
                )

            else:
                print(
                    f"❌ CASE {case_name} 失敗"
                )

                failed.append(
                    case_name
                )

        except Exception as e:
            print(
                f"❌ CASE {case_name}: {e}"
            )

            failed.append(
                case_name
            )

        time.sleep(1)

    print()
    print(
        "=============================="
    )
    print(
        "BATCH RESULT"
    )
    print(
        "=============================="
    )
    print(
        f"新規成功       : {len(success)}"
    )
    print(
        f"既存完全cache  : {len(skipped_valid)}"
    )
    print(
        "source不足skip : "
        f"{len(skipped_incomplete_source)}"
    )
    print(
        f"失敗           : {len(failed)}"
    )

    if failed:
        print()
        print(
            "失敗ケース:"
        )

        for case_name in failed:
            print(
                f"  {case_name}"
            )

    print(
        "=============================="
    )


if __name__ == "__main__":
    main()
