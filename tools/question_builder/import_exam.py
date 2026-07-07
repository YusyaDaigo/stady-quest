import argparse
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
    parser.add_argument("--start-page", type=int, default=2)
    parser.add_argument("--max-pages", type=int, default=999)
    parser.add_argument("--skip-build", action="store_true")

    args = parser.parse_args()

    exam = "pharmacy"
    category = "required"
    exam_number = args.exam

    question_pdf_path = Path(
        f"source_materials/{exam}/{category}/pdf/{exam_number}_required.pdf"
    )
    answer_pdf_path = Path(
        f"source_materials/{exam}/{category}/pdf/{exam_number}_answers.pdf"
    )

    if not question_pdf_path.exists():
        raise FileNotFoundError(f"問題PDFが見つかりません: {question_pdf_path}")

    if not answer_pdf_path.exists():
        raise FileNotFoundError(f"解答PDFが見つかりません: {answer_pdf_path}")

    print("==============================")
    print(f"🚀 Import Start: 第{exam_number}回 必須問題")
    print("==============================")

    run_past_exam_pipeline(
        exam=exam,
        category=category,
        exam_number=exam_number,
        question_pdf_path=question_pdf_path,
        answer_pdf_path=answer_pdf_path,
        vision_engine_name="openai",
        answer_parser="vision",
        start_page=args.start_page,
        max_pages=args.max_pages,
    )

    target_file = EXAM_PATHS[exam] / QUESTION_FILES[category]

    yearly_file = Path(
        f"src/exams/pharmacy/questions/required_{exam_number}.js"
    )

    validate_exam_import(
        target_file=yearly_file if yearly_file.exists() else target_file,
        exam_number=exam_number,
        expected_count=90,
    )

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
