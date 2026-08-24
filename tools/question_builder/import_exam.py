import argparse
import os
import subprocess
import sys
from pathlib import Path

from pipelines.past_exam_pipeline import run_past_exam_pipeline
from config import EXAM_PATHS, QUESTION_FILES
from validators.exam_import_validator import validate_exam_import


def refresh_required_index():
    base = Path("src/exams/pharmacy/questions")
    yearly_files = sorted(
        base.glob("required_*.js"),
        reverse=True,
    )

    imports = []
    spreads = []

    for file in yearly_files:
        exam_number = file.stem.replace("required_", "")
        export_name = f"required{exam_number}Questions"

        imports.append(
            f'import {{ {export_name} }} from "./required_{exam_number}";'
        )
        spreads.append(f"  ...{export_name},")

    index_file = base / "required.js"
    index_file.write_text(
        "\n".join(imports)
        + "\n\nexport const requiredQuestions = [\n"
        + "\n".join(spreads)
        + "\n];\n",
        encoding="utf-8",
    )

    print("🔄 required.js 更新完了")


def run_build():
    print("🏗️ npm run build 実行中...")
    result = subprocess.run(["npm", "run", "build"])
    if result.returncode != 0:
        raise RuntimeError("npm run build に失敗しました")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int, required=True)

    parser.add_argument(
        "--category",
        choices=["required", "theory", "practical"],
        default="required",
    )

    parser.add_argument(
        "--part",
        type=int,
        choices=[1, 2, 3],
        default=None,
        help="理論・実践問題のPDF分割番号",
    )

    parser.add_argument("--start-page", type=int, default=2)
    parser.add_argument("--max-pages", type=int, default=999)
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument(
        "--use-api",
        action="store_true",
        help="OpenAI APIを使用してキャッシュを生成する",
)

    args = parser.parse_args()

    if args.use_api:
        print("🌐 APIモード")
    else:
        os.environ["STUDY_QUEST_NO_API"] = "1"
        print("🛡️ NO_APIモード（デフォルト）")

    exam = "pharmacy"
    category = args.category
    exam_number = args.exam

    part = args.part

    if category == "required":
        question_pdf_path = Path(
            f"source_materials/{exam}/{category}/pdf/"
            f"{exam_number}_{category}.pdf"
        )
    else:
        if part is None:
            raise ValueError(
                f"{category} では --part の指定が必要です"
            )

        question_pdf_path = Path(
            f"source_materials/{exam}/{category}/pdf/"
            f"{exam_number}_{category}_{part}.pdf"
        )

    answer_pdf_path = Path(
        f"source_materials/{exam}/{category}/pdf/{exam_number}_answers.pdf"
    )
    if not question_pdf_path.exists():
        raise FileNotFoundError(f"問題PDFが見つかりません: {question_pdf_path}")

    if not answer_pdf_path.exists():
        raise FileNotFoundError(f"解答PDFが見つかりません: {answer_pdf_path}")

    print("==============================")
    print(
        f"🚀 Import Start: 第{exam_number}回 {category.upper()}"
    )
    print("==============================")

    run_past_exam_pipeline(
        exam=exam,
        category=category,
        exam_number=exam_number,
        question_pdf_path=question_pdf_path,
        answer_pdf_path=answer_pdf_path,
        part=part,
        vision_engine_name="openai",
        answer_parser="text",
        start_page=args.start_page,
        max_pages=args.max_pages,
    )

    if exam == "pharmacy":
        target_file = EXAM_PATHS[exam] / f"{category}_{exam_number}.js"

        export_names = {
            "required": f"required{exam_number}Questions",
            "theory": f"theory{exam_number}Questions",
            "practical": f"practical{exam_number}Questions",
        }

        export_name = export_names[category]

        if not target_file.exists():
            target_file.write_text(
                f'import {{ CATEGORIES }} from "./categories";\n\n'
                f'export const {export_name} = [\n\n'
                f'  // AI_QUESTION_INSERT_HERE\n'
                f'];\n',
                encoding="utf-8",
            )
    else:
        target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]


    yearly_file = Path(
        f"src/exams/pharmacy/questions/{category}_{exam_number}.js"
    )

    expected_counts = {
        "required": 90,
        "theory": 105,
        "practical": 150,
    }

    start_questions = {
        "required": 1,
        "theory": 91,
        "practical": 196,
    }

    excluded_questions = {
        ("theory", 111): [92],
        ("practical", 111): [199, 287],
    }

    validate_exam_import(
        target_file=yearly_file if yearly_file.exists() else target_file,
        exam_number=exam_number,
        expected_count=expected_counts[category],
        start_question=start_questions[category],
        excluded_numbers=excluded_questions.get(
            (category, exam_number),
            [],
        ),
    )

    if category == "required":
        refresh_required_index()

    if not args.skip_build:
        run_build()

    print("==============================")
    print(f"✅ Import Complete: 第{exam_number}回")
    print("==============================")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Import Failed: {e}", file=sys.stderr)
        raise
