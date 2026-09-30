import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

CACHE_ROOT = (
    ROOT
    / "tools"
    / "question_builder"
    / "cache"
    / "pharmacy"
    / "practical"
    / "cases"
)

QUESTION_ROOT = (
    ROOT
    / "src"
    / "exams"
    / "pharmacy"
    / "questions"
)


def escape_js_text(value):
    if value is None:
        return ""

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "\\n")
    )


def load_complete_case_cache(exam_number):
    cache_dir = CACHE_ROOT / str(exam_number)

    result = {}

    if not cache_dir.exists():
        return result

    for path in sorted(cache_dir.glob("*.json")):
        try:
            data = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        except Exception:
            continue

        case_id = data.get("case_id")
        case_context = data.get("case_context")
        questions = data.get("questions")

        if (
            not isinstance(case_id, str)
            or not case_id.strip()
            or not isinstance(case_context, str)
            or not case_context.strip()
            or not isinstance(questions, list)
            or len(questions) < 2
        ):
            continue

        case_match = re.search(
            r"-(\d+)-(\d+)$",
            case_id.strip(),
        )

        if not case_match:
            continue

        first_question_no = int(
            case_match.group(1)
        )
        last_question_no = int(
            case_match.group(2)
        )

        if last_question_no <= first_question_no:
            continue

        expected_question_numbers = list(
            range(
                first_question_no,
                last_question_no + 1,
            )
        )

        normalized = []

        valid = True

        for question in questions:
            question_no = question.get(
                "question_no"
            )
            question_text = question.get(
                "question"
            )
            choices = question.get(
                "choices"
            )

            if (
                not isinstance(
                    question_no,
                    int,
                )
                or not isinstance(
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
                valid = False
                break

            normalized.append(
                {
                    "question_no":
                        question_no,
                    "question":
                        question_text.strip(),
                    "choices":
                        choices,
                    "case_id":
                        case_id.strip(),
                    "case_context":
                        case_context.strip(),
                    "cache_file":
                        path.name,
                }
            )

        if not valid:
            continue

        actual_question_numbers = sorted(
            question["question_no"]
            for question in normalized
        )

        if (
            actual_question_numbers
            != expected_question_numbers
        ):
            continue

        for question in normalized:
            question_no = question[
                "question_no"
            ]

            if question_no in result:
                raise RuntimeError(
                    "duplicate cached question: "
                    f"Q{question_no}"
                )

            result[question_no] = question

    return result


def find_question_blocks(text):
    starts = [
        match.start()
        for match in re.finditer(
            r"(?m)^  \{$",
            text,
        )
    ]

    blocks = []

    for index, start in enumerate(starts):
        end = (
            starts[index + 1]
            if index + 1 < len(starts)
            else text.rfind("\n];")
        )

        if end <= start:
            continue

        block = text[start:end]

        match = re.search(
            r"(?m)^    sourceNumber: "
            r"(\d+),$",
            block,
        )

        if not match:
            continue

        blocks.append(
            {
                "source_number":
                    int(match.group(1)),
                "start":
                    start,
                "end":
                    end,
                "text":
                    block,
            }
        )

    return blocks


def build_case_fields(data):
    case_id = escape_js_text(
        data["case_id"]
    )

    case_context = escape_js_text(
        data["case_context"]
    )

    return (
        f'    caseId: "{case_id}",\n'
        "    caseContext:\n"
        f'      "{case_context}",'
    )


def build_question_field(data):
    question = escape_js_text(
        data["question"]
    )

    return (
        "    question:\n"
        f'      "{question}",'
    )


def build_choices_field(data):
    rows = []

    for choice in data["choices"]:
        rows.append(
            "    "
            + json.dumps(
                str(choice),
                ensure_ascii=False,
            )
            + ","
        )

    if rows:
        rows[-1] = rows[-1].rstrip(",")

    return (
        "    choices: [\n"
        + "\n".join(rows)
        + "\n"
        + "    ],"
    )


def replace_question_and_choices(
    block,
    data,
):
    pattern = re.compile(
        r'(?ms)^    question:\n'
        r'      ".*?",\n\n'
        r'^    choices: \[\n'
        r'.*?'
        r'^    \],'
    )

    replacement = (
        build_question_field(data)
        + "\n\n"
        + build_choices_field(data)
    )

    new_block, count = pattern.subn(
        lambda _match: replacement,
        block,
        count=1,
    )

    if count != 1:
        raise RuntimeError(
            "question/choices block "
            "not found"
        )

    return new_block


def replace_or_insert_case_fields(
    block,
    data,
):
    new_fields = build_case_fields(
        data
    )

    # 既存case metadataは形式を問わず一度すべて除去する。
    # 旧データには
    #
    #   caseContext:
    #     `複数行...`,
    #
    # のtemplate literal形式があり、新生成データには
    #
    #   caseContext:
    #     "...\n...",
    #
    # のquoted string形式がある。
    #
    # 重複したcase metadataが存在する場合も全件除去してから
    # 正規化済みの1組だけを挿入する。
    existing_pattern = re.compile(
        r'(?ms)'
        r'^    caseId: "[^"\n]*",\n'
        r'^    caseContext:'
        r'(?:'
        r'\n      "(?:\\.|[^"\\])*",'
        r'|'
        r'\n      `.*?`,'
        r'|'
        r' "(?:\\.|[^"\\])*",'
        r')'
        r'\n?'
    )

    cleaned_block, removed_count = (
        existing_pattern.subn(
            "",
            block,
        )
    )

    source_pattern = re.compile(
        r"(?m)^    sourceNumber: "
        r"\d+,$"
    )

    match = source_pattern.search(
        cleaned_block
    )

    if not match:
        raise RuntimeError(
            "sourceNumber not found"
        )

    insert_at = match.end()

    result = (
        cleaned_block[:insert_at]
        + "\n"
        + new_fields
        + cleaned_block[insert_at:]
    )

    return result


def load_context_only_case_cache(
    exam_number,
):
    cache_dir = (
        CACHE_ROOT / str(exam_number)
    )

    result = {}

    if not cache_dir.exists():
        return result

    for path in sorted(
        cache_dir.glob("*.json")
    ):
        try:
            data = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        except Exception:
            continue

        case_id = data.get(
            "case_id"
        )
        case_context = data.get(
            "case_context"
        )
        questions = data.get(
            "questions"
        )

        if (
            not isinstance(
                case_id,
                str,
            )
            or not case_id.strip()
            or not isinstance(
                case_context,
                str,
            )
            or not case_context.strip()
        ):
            continue

        match = re.fullmatch(
            rf"{exam_number}-(\d+)-(\d+)",
            case_id,
        )

        if not match:
            continue

        first = int(
            match.group(1)
        )
        second = int(
            match.group(2)
        )

        if second <= first:
            continue

        expected_question_numbers = list(
            range(
                first,
                second + 1,
            )
        )

        actual_question_numbers = []

        if isinstance(
            questions,
            list,
        ):
            for question in questions:
                if not isinstance(
                    question,
                    dict,
                ):
                    actual_question_numbers = []
                    break

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
                    actual_question_numbers = []
                    break

                actual_question_numbers.append(
                    question_no
                )

        # 完全cacheは既存処理へ任せる。
        if (
            sorted(
                actual_question_numbers
            )
            == expected_question_numbers
        ):
            continue

        result[
            (first, second)
        ] = {
            "case_id":
                case_id.strip(),
            "case_context":
                case_context.strip(),
        }

    return result


def strip_context_prefix(
    question_text,
    case_context,
):
    if (
        not question_text
        or not case_context
    ):
        return question_text

    q = str(
        question_text
    )
    c = str(
        case_context
    )

    qi = 0
    ci = 0

    while (
        qi < len(q)
        and ci < len(c)
    ):
        while (
            qi < len(q)
            and q[qi].isspace()
        ):
            qi += 1

        while (
            ci < len(c)
            and c[ci].isspace()
        ):
            ci += 1

        if (
            qi >= len(q)
            or ci >= len(c)
        ):
            break

        if q[qi] != c[ci]:
            return question_text

        qi += 1
        ci += 1

    while (
        ci < len(c)
        and c[ci].isspace()
    ):
        ci += 1

    if ci != len(c):
        return question_text

    remainder = q[qi:].strip()

    if not remainder:
        return question_text

    return remainder


def repair_exam(
    exam_number,
    dry_run,
):
    target = (
        QUESTION_ROOT
        / f"practical_{exam_number}.js"
    )

    if not target.exists():
        raise FileNotFoundError(
            target
        )

    cache_questions = (
        load_complete_case_cache(
            exam_number
        )
    )

    context_only_cases = (
        load_context_only_case_cache(
            exam_number
        )
    )

    original = target.read_text(
        encoding="utf-8"
    )

    blocks = find_question_blocks(
        original
    )

    block_map = {
        block["source_number"]: block
        for block in blocks
    }

    missing = sorted(
        set(cache_questions)
        - set(block_map)
    )

    if missing:
        raise RuntimeError(
            "generated JS missing cached "
            "questions: "
            + ", ".join(
                f"Q{number}"
                for number in missing
            )
        )

    replacements = []
    changed_numbers = []

    #
    # 完全な2問case
    #
    for question_no in sorted(
        cache_questions
    ):
        data = cache_questions[
            question_no
        ]

        block_info = block_map[
            question_no
        ]

        old_block = block_info[
            "text"
        ]

        new_block = (
            replace_or_insert_case_fields(
                old_block,
                data,
            )
        )

        new_block = (
            replace_question_and_choices(
                new_block,
                data,
            )
        )

        if new_block != old_block:
            changed_numbers.append(
                question_no
            )

        replacements.append(
            (
                block_info["start"],
                block_info["end"],
                new_block,
            )
        )

    #
    # 片割れが除外されたcontext-only case
    #
    partial_case_numbers = []

    for (
        first,
        second
    ), case_data in sorted(
        context_only_cases.items()
    ):
        existing_numbers = [
            number
            for number in (
                first,
                second,
            )
            if number in block_map
        ]

        # 両方あるなら完全cache側で扱うべき。
        # 両方ないなら何もしない。
        if len(existing_numbers) != 1:
            continue

        question_no = (
            existing_numbers[0]
        )

        # 完全cacheで既に処理済みなら触らない。
        if question_no in cache_questions:
            continue

        block_info = block_map[
            question_no
        ]

        old_block = block_info[
            "text"
        ]

        data = {
            "case_id":
                case_data["case_id"],
            "case_context":
                case_data[
                    "case_context"
                ],
        }

        new_block = (
            replace_or_insert_case_fields(
                old_block,
                data,
            )
        )

        #
        # question本文にcaseContextが
        # 丸ごと重複している場合のみ、
        # そのprefixを安全に除去する。
        #
        question_pattern = re.compile(
            r'(?ms)'
            r'^    question:\n'
            r'      "'
            r'((?:\\.|[^"\\])*)'
            r'",'
        )

        match = (
            question_pattern.search(
                new_block
            )
        )

        if match:
            raw_question = (
                match.group(1)
            )

            try:
                question_text = (
                    json.loads(
                        '"'
                        + raw_question
                        + '"'
                    )
                )
            except Exception:
                question_text = (
                    raw_question
                )

            stripped_question = (
                strip_context_prefix(
                    question_text,
                    data[
                        "case_context"
                    ],
                )
            )

            if (
                stripped_question
                != question_text
            ):
                replacement = (
                    '    question:\n'
                    '      "'
                    + escape_js_text(
                        stripped_question
                    )
                    + '",'
                )

                new_block, count = (
                    question_pattern.subn(
                        lambda _match:
                            replacement,
                        new_block,
                        count=1,
                    )
                )

                if count != 1:
                    raise RuntimeError(
                        "question replacement "
                        f"failed: Q{question_no}"
                    )

        if new_block != old_block:
            changed_numbers.append(
                question_no
            )

        partial_case_numbers.append(
            question_no
        )

        replacements.append(
            (
                block_info["start"],
                block_info["end"],
                new_block,
            )
        )

    updated = original

    for (
        start_pos,
        end_pos,
        replacement,
    ) in sorted(
        replacements,
        reverse=True,
    ):
        updated = (
            updated[:start_pos]
            + replacement
            + updated[end_pos:]
        )

    print(
        "=============================="
    )
    print(
        f"PRACTICAL CASE REPAIR {exam_number}"
    )
    print(
        "=============================="
    )

    print(
        "complete cache questions :",
        len(cache_questions),
    )

    print(
        "partial case questions  :",
        len(partial_case_numbers),
    )

    if partial_case_numbers:
        print(
            "partial sourceNumbers   :",
            ", ".join(
                str(number)
                for number
                in partial_case_numbers
            ),
        )

    print(
        "changed questions        :",
        len(changed_numbers),
    )

    if changed_numbers:
        print(
            "changed sourceNumbers   :",
            ", ".join(
                str(number)
                for number
                in sorted(
                    set(
                        changed_numbers
                    )
                )
            ),
        )

    if updated == original:
        print(
            "変更なし"
        )
        return

    if dry_run:
        print(
            "DRY RUN: "
            "ファイルは書き換えていません"
        )
        return

    target.write_text(
        updated,
        encoding="utf-8",
    )

    print(
        f"✅ updated: {target}"
    )

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

    repair_exam(
        exam_number=args.exam,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
