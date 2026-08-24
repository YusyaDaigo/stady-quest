import argparse
import json
import re
from pathlib import Path

from vision.openai_vision import analyze_practical_case


CACHE_ROOT = Path(
    "tools/question_builder/cache/pharmacy/practical/vision"
)

IMAGE_ROOT = Path(
    "source_materials/pharmacy/practical/images"
)

CASE_CACHE_ROOT = Path(
    "tools/question_builder/cache/pharmacy/practical/cases"
)


def extract_page_number(path: Path) -> int:
    match = re.search(
        r"page_(\d+)\.json$",
        path.name,
    )

    if not match:
        raise ValueError(
            f"ページ番号を取得できません: {path}"
        )

    return int(match.group(1))


def load_question_numbers(cache_path: Path):
    try:
        data = json.loads(
            cache_path.read_text(encoding="utf-8")
        )
    except Exception:
        return set()

    if isinstance(data, dict):
        if "questions" in data:
            data = data["questions"]
        else:
            data = [data]

    if not isinstance(data, list):
        return set()

    result = set()

    for item in data:
        if not isinstance(item, dict):
            continue

        question_no = item.get("question_no")

        if isinstance(question_no, int):
            result.add(question_no)

    return result


def find_related_pages(
    exam_number: int,
    first_question_no: int,
    second_question_no: int,
):
    exam_cache_root = (
        CACHE_ROOT / str(exam_number)
    )

    targets = {
        first_question_no,
        second_question_no,
    }

    found = []

    for cache_path in sorted(
        exam_cache_root.rglob("page_*.json")
    ):
        question_numbers = load_question_numbers(
            cache_path
        )

        if targets & question_numbers:
            found.append(cache_path)

    if not found:
        raise RuntimeError(
            "関連Vision cacheが見つかりません: "
            f"{first_question_no}-{second_question_no}"
        )

    parts = {
        cache_path.parent.name
        for cache_path in found
    }

    if len(parts) != 1:
        raise RuntimeError(
            "複数partにまたがるケースです: "
            f"{first_question_no}-{second_question_no} "
            f"{sorted(parts)}"
        )

    part_name = next(iter(parts))

    page_numbers = sorted(
        extract_page_number(path)
        for path in found
    )

    # 症例本文が設問より前のページにあることがあるため
    # 前1ページを必ず含める。
    start_page = max(
        1,
        min(page_numbers) - 1,
    )

    # 後続ページに選択肢等が続く場合に備えて
    # 最後の関連ページの次も1ページ含める。
    end_page = max(page_numbers) + 1

    image_dir = (
        IMAGE_ROOT
        / str(exam_number)
        / part_name
    )

    image_paths = []

    for page_no in range(
        start_page,
        end_page + 1,
    ):
        image_path = (
            image_dir
            / f"page_{page_no}.png"
        )

        if image_path.exists():
            image_paths.append(image_path)

    if not image_paths:
        raise RuntimeError(
            "解析対象画像が見つかりません"
        )

    return (
        part_name,
        image_paths,
    )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--exam",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--first",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--second",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--force",
        action="store_true",
    )

    args = parser.parse_args()

    output_path = (
        CASE_CACHE_ROOT
        / str(args.exam)
        / f"{args.first}-{args.second}.json"
    )

    if (
        output_path.exists()
        and not args.force
    ):
        print(
            f"📦 case cache既存: {output_path}"
        )
        print(
            "再解析する場合は --force を付けてください"
        )
        return

    part_name, image_paths = (
        find_related_pages(
            exam_number=args.exam,
            first_question_no=args.first,
            second_question_no=args.second,
        )
    )

    print("==============================")
    print(
        f"CASE ANALYSIS: "
        f"{args.first}-{args.second}"
    )
    print(
        f"Part: {part_name}"
    )
    print("Images:")

    for image_path in image_paths:
        print(
            f"  {image_path}"
        )

    print("==============================")

    result = analyze_practical_case(
        image_paths=image_paths,
        first_question_no=args.first,
        second_question_no=args.second,
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print(
        f"✅ case cache保存: {output_path}"
    )

    print()
    print("===== caseContext =====")
    print(
        result.get(
            "case_context",
            ""
        )
    )


if __name__ == "__main__":
    main()
