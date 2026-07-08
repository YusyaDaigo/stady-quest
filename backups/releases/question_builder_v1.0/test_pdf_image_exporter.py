from pathlib import Path

from parsers.pdf_image_exporter import export_pdf_pages_to_images


pdf_path = Path("source_materials/pharmacy/required/pdf/111_required.pdf")
output_dir = Path("source_materials/pharmacy/required/images/111_required")

paths = export_pdf_pages_to_images(
    pdf_path=pdf_path,
    output_dir=output_dir,
    max_pages=3,
)

print("出力画像:")
for path in paths:
    print(path)