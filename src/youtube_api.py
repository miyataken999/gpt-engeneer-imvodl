import os
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_video_transcript(self, video_id):
        request = self.youtube.captions().list(
            part="id,snippet",
            videoId=video_id
        )
        response = request.execute()
        captions = response["items"]
        for caption in captions:
            if caption["snippet"]["languageCode"] == "ja":
                caption_id = caption["id"]["captionId"]
                request = self.youtube.captions().get(
                    id=caption_id
                )
                response = request.execute()
                return response["snippet"]["textBody"]
        return None