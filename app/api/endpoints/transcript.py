from app.services.transcript_service import process_transcript, get_transcript_row
from app.repositories.transcript_repository import TranscriptRepository
from fastapi import APIRouter, HTTPException, Depends
from app.utils.db_utils import get_db_connection
from psycopg2.extensions import connection

router = APIRouter()


@router.post("/{video_id}")
async def get_and_save_transcript(
    video_id: str, db_client: connection = Depends(get_db_connection)
):
    """
    Fetches the transcript for a given YouTube video ID.
    """
    try:
        repository = TranscriptRepository(db_client)
        transcript = await process_transcript(video_id, repository)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{video_id}")
async def get_transcript_from_db(
    video_id: str, db_client: connection = Depends(get_db_connection)
):
    """
    Fetches a transcript by video ID.
    """
    try:
        repository = TranscriptRepository(db_client)
        transcript = await get_transcript_row(video_id, repository)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        print(f"Error fetching transcript in out database: {e}")
        raise HTTPException(status_code=500, detail=str(e))
