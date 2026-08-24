import json
import subprocess
import sys
import time
from pathlib import Path


TARGET_PAIRS = [
    (198, 199),
    (200, 201),
    (202, 203),
    (204, 205),
    (206, 207),
    (208, 209),
    (212, 213),
    (214, 215),
    (216, 217),
    (220, 221),
    (222, 223),
    (226, 227),
    (234, 235),
    (236, 237),
    (242, 243),
    (246, 247),
    (250, 251),
    (252, 253),
    (254, 255),
    (256, 257),
    (264, 265),
    (266, 267),
    (268, 269),
    (270, 271),
    (272, 273),
    (276, 277),
    (280, 281),
    (282, 283),
    (288, 289),
    (294, 295),
    (298, 299),
    (300, 301),
    (306, 307),
    (308, 309),
    (314, 315),
    (316, 317),
    (322, 323),
    (324, 325),
    (326, 327),
    (328, 329),
    (332, 333),
    (334, 335),
    (336, 337),
    (342, 343),
    (344, 345),
]


CASE_CACHE_ROOT = Path(
    "tools/question_builder/cache/pharmacy/"
    "practical/cases/111"
)

REBUILD_SCRIPT = Path(
    "tools/question_builder/scripts/"
    "rebuild_practical_case_cache.py"
)


def is_valid_case_cache(path: Path) -> bool:
    if not path.exists():
        return False

    try:
        data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except Exception:
        return False

    case_context = data.get("case_context", "")

    if not isinstance(case_context, str):
        return False

    context = case_context.strip()

    if not context:
        return False

    invalid_phrases = [
        "画像内に2問共通の症例",
        "確認できない",
        "提示されていない",
    ]

    if any(
        phrase in context
        for phrase in invalid_phrases
    ):
        return False

    return True


def main():
    CASE_CACHE_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    success = []
    skipped = []
    failed = []

    total = len(TARGET_PAIRS)

    print("==============================")
    print("PRACTICAL CASE BATCH REBUILD")
    print("==============================")
    print(f"対象ケース数: {total}")
    print("==============================")
    print()

    for index, (first_no, second_no) in enumerate(
        TARGET_PAIRS,
        start=1,
    ):
        case_name = f"{first_no}-{second_no}"

        cache_path = (
            CASE_CACHE_ROOT
            / f"{case_name}.json"
        )

        print()
        print(
            f"[{index}/{total}] "
            f"CASE {case_name}"
        )

        if is_valid_case_cache(cache_path):
            print(
                f"📦 有効cacheあり: {cache_path}"
            )

            skipped.append(case_name)
            continue

        command = [
            sys.executable,
            str(REBUILD_SCRIPT),
            "--exam",
            "111",
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
                    cache_path
                )
            ):
                print(
                    f"✅ CASE {case_name} 完了"
                )

                success.append(case_name)

            else:
                print(
                    f"❌ CASE {case_name} 失敗"
                )

                failed.append(case_name)

        except Exception as e:
            print(
                f"❌ CASE {case_name}: {e}"
            )

            failed.append(case_name)

        # APIへの連続負荷を少し抑える
        time.sleep(1)

    print()
    print("==============================")
    print("BATCH RESULT")
    print("==============================")
    print(
        f"新規成功 : {len(success)}"
    )
    print(
        f"既存cache: {len(skipped)}"
    )
    print(
        f"失敗     : {len(failed)}"
    )

    if failed:
        print()
        print("失敗ケース:")
        for case_name in failed:
            print(
                f"  {case_name}"
            )

    print("==============================")


if __name__ == "__main__":
    main()
