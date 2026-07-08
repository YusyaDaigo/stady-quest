import argparse
import sys
from pathlib import Path

from parsers.pdf_image_exporter import export_pdf_pages_to_images
from vision.cached_openai_vision import analyze_page


def build_vision_cache(
    exam_number: int,
    start_page: int = 2,
    max_pages: int = 999,
):
    question_pdf_path = Path(
        f"source_materials/pharmacy/required/pdf/{exam_number}_required.pdf"
    )

    if not question_pdf_path.exists():
        raise FileNotFoundError(
            f"問題PDFが見つかりません: {question_pdf_path}"
        )

    image_output_dir = Path(
        f"source_materials/pharmacy/required/images/{exam_number}"
    )

    image_paths = export_pdf_pages_to_images(
        pdf_path=question_pdf_path,
        output_dir=image_output_dir,
        max_pages=start_page + max_pages - 1,
    )

    target_image_paths = image_paths[
        start_page - 1:start_page - 1 + max_pages
    ]

    print("==============================")
    print(f"🚀 Vision Cache Build: 第{exam_number}回 必須問題")
    print("==============================")

    success_count = 0
    failed_pages = []

    for image_path in target_image_paths:
        print(f"📄 Vision解析/cache確認: {image_path}")

        try:
            analyze_page(image_path)
            success_count += 1

        except Exception as e:
            print(f"⚠️ Vision cache作成失敗: {image_path}: {e}")
            failed_pages.append(str(image_path))

            # quota切れの場合、以後も失敗する可能性が高いので停止
            if "quota" in str(e).lower() or "429" in str(e):
                print("🛑 API quota切れの可能性が高いため停止します")
                break

    print("==============================")
    print(f"✅ Success pages: {success_count}")
    print(f"⚠️ Failed pages : {len(failed_pages)}")

    if failed_pages:
        print("Failed page list:")
        for page in failed_pages:
            print(page)

    print("==============================")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--start-page", type=int, default=2)
    parser.add_argument("--max-pages", type=int, default=999)

    args = parser.parse_args()

    if args.all:
        for exam_number in range(97, 112):
            build_vision_cache(
                exam_number=exam_number,
                start_page=args.start_page,
                max_pages=args.max_pages,
            )
        return

    if args.exam is None:
        raise SystemExit("--exam または --all を指定してください")

    build_vision_cache(
        exam_number=args.exam,
        start_page=args.start_page,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Vision Cache Build Failed: {e}", file=sys.stderr)
        raise
