# app/services/transcript_service.py

from youtube_transcript_api import YouTubeTranscriptApi
from app.repositories.transcript_repository import TranscriptRepository


def fetch_transcript(video_id: str) -> dict:
    """Fetches the transcript for a given YouTube video ID.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        dict: The transcript as a list of dictionaries with time and text.

    Raises:
        RuntimeError: If fetching the transcript fails.
    """
    try:
        repository = TranscriptRepository()
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = "\n".join(
            [f"{item['start']:.2f}s: {item['text']}" for item in transcript]
        )

        transcript_dict = {
            "video_id": video_id,
            "transcript": transcript,
            "transcript_text": transcript_text,
        }

        repository.save_transcript(transcript_dict)

        print(transcript_text)

        return transcript
    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: {str(e)}")
