from app.services.transcript_service import fetch_transcript, get_transcript_row
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/{video_id}")
async def get_transcript(video_id: str):
    """
    Fetches the transcript for a given YouTube video ID.
    """
    try:
        transcript = await fetch_transcript(video_id)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{video_id}")
async def get_transcript_from_db(video_id: str):
    """
    Fetches a transcript by video ID.
    """
    try:
        transcript = await get_transcript_row(video_id)
        return {"video_id": video_id, "transcript": transcript}
        # return transcript
    except Exception as e:
        print(f"Error fetching transcript in out database: {e}")
        raise HTTPException(status_code=500, detail=str(e))
