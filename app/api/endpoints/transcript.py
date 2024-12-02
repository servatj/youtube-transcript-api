from fastapi import APIRouter, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

router = APIRouter()


@router.get("/{video_id}")
async def fetch_transcript(video_id: str):
    """
    Fetches the transcript for a given YouTube video ID.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
