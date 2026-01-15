class RagObserver:
    """
    Rag watches, reacts, and remembers.
    """
    def __init__(self):
        self.mood = "neutral"

    def observe(self, message: str):
        return f"Rag tilts her head: '{message}'"
