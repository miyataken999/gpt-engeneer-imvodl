import re

class TranscriptProcessor:
    def __init__(self):
        pass

    def process_transcript(self, transcript):
        # Remove timestamps and newline characters
        transcript = re.sub(r"\n", "", transcript)
        transcript = re.sub(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", transcript)
        return transcript