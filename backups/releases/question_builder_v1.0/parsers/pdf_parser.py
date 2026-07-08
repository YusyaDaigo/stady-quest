from pypdf import PdfReader


def calculate_garbled_score(text: str) -> float:
    if not text:
        return 1.0

    suspicious_chars = [
        "�",
        "ø",
        "ù",
        "ú",
        "û",
        "ü",
        "Ā",
        "ʕ",
        "ɹ",
        "ͯ",
        "ͷ",
        "͸",
    ]

    suspicious_count = sum(
        text.count(char)
        for char in suspicious_chars
    )

    return suspicious_count / max(len(text), 1)


def is_garbled_text(text: str, threshold: float = 0.02) -> bool:
    return calculate_garbled_score(text) >= threshold


def extract_pdf_text(pdf_path):
    reader = PdfReader(str(pdf_path))

    text_parts = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)

    return "\n".join(text_parts)


def parse_pdf_material(pdf_path):
    full_text = extract_pdf_text(pdf_path)

    garbled_score = calculate_garbled_score(full_text)
    garbled = is_garbled_text(full_text)

    print("===== PDF ANALYSIS =====")
    print(f"PDF: {pdf_path}")
    print(f"文字数: {len(full_text)}")
    print(f"文字化けスコア: {garbled_score:.4f}")
    print(f"判定: {'garbled' if garbled else 'usable'}")
    print("===== PDF TEXT PREVIEW =====")
    print(full_text[:1500])
    print("===== END PREVIEW =====")

    return []