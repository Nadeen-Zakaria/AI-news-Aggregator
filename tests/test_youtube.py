from src.services.youtube import search_videos
from src.services.youtube_transcript import get_transcript


videos = search_videos("Artificial Intelligence", 5)

for video in videos:
    video_id = video["id"]["videoId"]
    title = video["snippet"]["title"]

    print("\nTITLE:", title)
    print("VIDEO ID:", video_id)
    
    try:
        transcript= get_transcript(video_id)
        
        print ("Transcript: ")
        print(transcript[:1000])
        
    except Exception as e:
        print("Transcript is unavailable: ",e)
        
    
    