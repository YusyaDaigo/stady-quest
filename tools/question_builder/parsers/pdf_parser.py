from pypdf import PdfReader


def parse_pdf_material(pdf_path):
    reader = PdfReader(str(pdf_path))

    text_parts = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)

    full_text = "\n".join(text_parts)

    print("===== PDF TEXT PREVIEW =====")
    print(full_text[:3000])
    print("===== END PREVIEW =====")

    return []