import os
from pytube import YouTube

class YouTuber:
    def __init__(self, url):
        self.url = url
        self.youtube = YouTube(url)

    def download_captions(self):
        captions = self.youtube.captions.get_by_language_code('ja')
        return captions.generate_srt_captions()