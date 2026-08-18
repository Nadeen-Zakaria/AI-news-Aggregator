from src.services.youtube_transcript import get_transcript


video_id = "E8zpgNPx8jE"

transcript = get_transcript(video_id)

print(transcript)