
# app/api/endpoints/analyze.py

from fastapi import APIRouter, HTTPException
from app.services.openai_service import analyze_transcript

router = APIRouter()

@router.post("/")
async def analyze_transcript_endpoint(transcript: str):
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
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")