def detect_emotion(text: str):
    if "!" in text:
        return "excited"
    if "..." in text:
        return "suspicious"
    return "neutral"
