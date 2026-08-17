from src.services.youtube import search_videos


videos = search_videos("artificial intelligence", 5)

for video in videos:
    print(video["snippet"]["title"])