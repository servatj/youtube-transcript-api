# app/api/endpoints/analyze.py

from multiprocessing import connection
from fastapi import APIRouter, Depends, HTTPException
from app.models.transcript import TranscriptRequest
from app.repositories.analyze_repository import AnalyzeRepository
from app.repositories.transcript_repository import TranscriptRepository
from app.services.openai_service import analyze_transcript
from app.services.transcript_service import get_transcript_row
from app.utils.db_utils import get_db_connection

router = APIRouter()

# Define the request body schema


@router.post("/structured")
async def analyze_transcript_endpoint(
    request: TranscriptRequest, db_client: connection = Depends(get_db_connection)
):
    """
    Endpoint to analyze a given transcript (structured as a list of text segments) for key topics.

    Args:
        request (TranscriptRequest): The transcript request body containing a list of text segments.

    Returns:
        dict: Analysis results including key topics.
    """
    try:
        # Combine the text segments into a single string
        full_transcript = " ".join([item.text for item in request.transcript])

        # Pass the combined text to the analyzer
        analysis_result = analyze_transcript(full_transcript)
        return {"transcript": full_transcript, "analysis": analysis_result}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.post("/raw")
async def analyze_transcript_endpoint_raw(transcript: str):
    """
    Endpoint to analyze a given transcript for key topics.

    Args:
        transcript (str): The transcript text to analyze.

    Returns:
        dict: Analysis results including key topics.
    """
    try:
        analysis_result = analyze_transcript(transcript)
        return {"transcript": transcript, "analysis": analysis_result}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/analyze-video/{video_id}")
async def analyze_video_endpoint(
    video_id: str, db_client: connection = Depends(get_db_connection)
):
    """
    Endpoint to analyze a video by its ID.

    Args:
        video_id (str): The video ID to fetch and analyze the transcript for.
        db (Session): Database session.

    Returns:
        dict: Analysis results including key topics.
    """
    try:
        # Fetch transcript from the database
        print(f"Fetching transcript for video ID: {video_id}")
        repository = TranscriptRepository(db_client)
        transcript_record = await get_transcript_row(video_id, repository)
        if not transcript_record:
            raise HTTPException(
                status_code=404, detail=f"No transcript found for video ID {video_id}"
            )

        transcript_id = transcript_record[0]
        transcript = transcript_record[2]

        print(f"Transcript: {transcript}")

        repositore_analysis = AnalyzeRepository()

        # Analyze the transcript
        analysis_result = await analyze_transcript(
            transcript_id, {transcript: transcript}, video_id, repositore_analysis
        )

        return {
            "video_id": video_id,
            "transcript": transcript,
            "analysis": analysis_result,
        }

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
