from vision.mock_vision import analyze_page as mock_analyze_page
from vision.cached_openai_vision import analyze_page as openai_analyze_page


def get_vision_engine(name: str):
    if name == "mock":
        return mock_analyze_page

    if name == "openai":
        return openai_analyze_page

    raise ValueError(f"未対応のVision Engineです: {name}")
