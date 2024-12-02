# app/api/endpoints/analyze.py

from fastapi import APIRouter, HTTPException
from app.models.transcript import TranscriptRequest
from app.services.openai_service import analyze_transcript

router = APIRouter()

# Define the request body schema


@router.post("/structured")
async def analyze_transcript_endpoint(request: TranscriptRequest):
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
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
