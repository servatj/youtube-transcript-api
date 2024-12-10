# app/services/openai_service.py

import os
from openai import OpenAI
from app.core import settings
from app.repositories.analyze_repository import AnalyzeRepository

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
                {
                    "role": "system",
                    "content": "You are an assistant that summarizes transcripts.",
                },
                {
                    "role": "user",
                    "content": f"Summarize this transcript succinctly: {transcript}",
                },
            ],
            max_tokens=150,  # Optional: Limit the length of the summary to avoid overly verbose outputs
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Failed to summarize transcript: {str(e)}")


async def analyze_transcript(
    transcript_id: str, transcript: str, video_id: str, repository: AnalyzeRepository
) -> str:
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
        repository = AnalyzeRepository()
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Adjust to the latest model or version if available
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that analyzes transcripts for key topics.",
                },
                {
                    "role": "user",
                    "content": f"Analyze this transcript and extract key topics: {transcript}",
                },
            ],
            max_tokens=200,  # Optional: Limit the length of the analysis response
        )

        analysis_id = await repository.save_analysis(
            video_id, response.choices[0].message.content, transcript_id
        )
        print(f"Analysis saved with ID: {analysis_id}")
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Failed to analyze transcript: {str(e)}")


async def analyze_transcript_variable_content(
    transcript: str, user_analysis_description: str
) -> str:
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
                {
                    "role": "system",
                    "content": "You are an assistant that analyzes transcripts from youtube videos.",
                },
                {
                    "role": "user",
                    "content": f"{user_analysis_description} {transcript}",
                },
            ],
            max_tokens=200,  # Optional: Limit the length of the analysis response
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Failed to analyze transcript: {str(e)}")
