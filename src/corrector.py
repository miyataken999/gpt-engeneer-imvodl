import re

class Corrector:
    def __init__(self):
        pass

    def correct_transcript(self, transcript):
        # Simple correction rules
        transcript = re.sub(r"([。,、])", r" \1", transcript)
        transcript = re.sub(r"([!?])", r" \1", transcript)
        return transcript