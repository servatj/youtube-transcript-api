# app/services/openai_service.py

import openai
from app.core import settings

# Set the OpenAI API key from settings
openai.api_key = settings.OPENAI_API_KEY

def summarize_transcript(transcript: str) -> str:
    """Summarizes a given transcript using OpenAI's GPT model.

    Args:
        transcript (str): The full transcript text.

    Returns:
        str: A summarized version of the transcript.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if "gpt-4" is unavailable
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes transcripts."},
                {"role": "user", "content": f"Summarize this transcript: {transcript}"}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise RuntimeError(f"Failed to summarize transcript: {str(e)}")

def analyze_transcript(transcript: str) -> dict:
    """Analyzes a given transcript to extract key topics.

    Args:
        transcript (str): The full transcript text.

    Returns:
        dict: Analysis results including key topics.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if "gpt-4" is unavailable
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes transcripts."},
                {"role": "user", "content": f"Analyze this transcript and extract key topics: {transcript}"}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return {"analysis": response["choices"][0]["message"]["content"].strip()}
    except Exception as e:
        raise RuntimeError(f"Failed to analyze transcript: {str(e)}")
