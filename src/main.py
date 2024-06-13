import os
import json
from pytube import YouTube
from youtube_dl import YouTubeDL
from src.youtuber import YouTuber
from src.text_corrector import TextCorrector

def main():
    # Load configuration
    with open('config.json') as f:
        config = json.load(f)

    # Create YouTuber object
    youtuber = YouTuber(config['youtuber_url'])

    # Download YouTube video captions
    captions = youtuber.download_captions()

    # Correct captions
    corrector = TextCorrector()
    corrected_captions = corrector.correct(captions)

    # Save corrected captions to file
    with open('corrected_captions.txt', 'w') as f:
        f.write(corrected_captions)

if __name__ == '__main__':
    main()