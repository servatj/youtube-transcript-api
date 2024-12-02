# app/services/openai_service.py

import os
from openai import OpenAI
from app.core import settings

# Initialize the OpenAI client with the API key directly from settings or environment variable
client = OpenAI(api_key=settings.OPENAI_API_KEY or os.getenv("OPENAI_API_KEY"))

def summarize_transcript(transcript: str) -> str:
    """
    Summarizes a given transcript using OpenAI's latest model.

    Args:
        transcript (str): The full transcript text.

    Returns:
        str: A summarized version of the transcript.

    Raises:
        RuntimeError: If there's an error during the API call.
    """
    try:
        # Use the latest model or specify a version if you need to
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Adjust to the latest model or version if available
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes transcripts."},
                {"role": "user", "content": f"Summarize this transcript succinctly: {transcript}"}
            ],
            max_tokens=150,  # Optional: Limit the length of the summary to avoid overly verbose outputs
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Failed to summarize transcript: {str(e)}")

def analyze_transcript(transcript: str) -> str:
    """
    Analyzes a given transcript using OpenAI's latest model.

    Args:
        transcript (str): The full transcript text.

    Returns:
        str: Analysis results including key topics.

    Raises:
        RuntimeError: If there's an error during the API call.
    """
    try:
        # Use the latest model or specify a version if you need to
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Adjust to the latest model or version if available
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes transcripts for key topics."},
                {"role": "user", "content": f"Analyze this transcript and extract key topics: {transcript}"}
            ],
            max_tokens=200,  # Optional: Limit the length of the analysis response
        )
        return response.choices[0].message.content.strip(transcript)
    except Exception as e:
        raise RuntimeError(f"Failed to analyze transcript: {str(e)}")
    
def analyze_trasncript_variable_content(transcript: str, user_analysis_description: str) -> str:
    """
    Analyzes a given transcript using OpenAI's latest model.

    Args:
        transcript (str): The full transcript text.

    Returns:
        str: Analysis results including the.

    Raises:
        RuntimeError: If there's an error during the API call.
    """
    try:
        # Use the latest model or specify a version if you need to
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Adjust to the latest model or version if available
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes transcripts from youtube videos."},
                {"role": "user", "content": f"{user_analysis_description} {transcript}"}
            ],
            max_tokens=200,  # Optional: Limit the length of the analysis response
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Failed to analyze transcript: {str(e)}")
    