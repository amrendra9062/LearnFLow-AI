from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(url):
    video_id = url.split("v=")[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([t["text"] for t in transcript])
    return text