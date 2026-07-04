from vision.mock_vision import analyze_question_image as mock_analyze_question_image


def get_vision_engine(name: str):
    if name == "mock":
        return mock_analyze_question_image

    raise ValueError(f"未対応のVision Engineです: {name}")