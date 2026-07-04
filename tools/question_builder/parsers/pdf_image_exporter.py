from pathlib import Path

import fitz


def export_pdf_pages_to_images(pdf_path: Path, output_dir: Path, max_pages: int = 3):
    output_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)

    exported_paths = []

    for page_index in range(min(len(doc), max_pages)):
        page = doc[page_index]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        output_path = output_dir / f"page_{page_index + 1}.png"
        pix.save(output_path)

        exported_paths.append(output_path)

    return exported_paths