from vision.mock_vision import analyze_page as mock_analyze_page
from vision.cached_openai_vision import analyze_page as openai_analyze_page


def get_vision_engine(name: str):
    if name == "mock":
        def analyze(image_path, category="required"):
            return mock_analyze_page(image_path)

        return analyze

    if name == "openai":
        def analyze(image_path, category="required"):
            return openai_analyze_page(
                image_path,
                category=category,
            )

        return analyze

    raise ValueError(f"未対応のVision Engineです: {name}")
