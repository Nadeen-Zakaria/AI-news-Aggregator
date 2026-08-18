import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def search_videos(query, max_results=5):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    return response["items"]

def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )

    response = request.execute()

    if not response["items"]:
        return None

    return response["items"][0]