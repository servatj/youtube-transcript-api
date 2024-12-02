# app/services/transcript_service.py

from youtube_transcript_api import YouTubeTranscriptApi

from app.models.transcript import TranscriptRow, TranscriptYoutubeResponse
from app.repositories.transcript_repository import TranscriptRepository


async def fetch_transcript(video_id: str) -> TranscriptYoutubeResponse:
    """Fetches the transcript for a given YouTube video ID.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        dict: The transcript as a list of dictionaries with time and text.

    Raises:
        RuntimeError: If fetching the transcript fails.
    """
    method_name = "transcript_service/fetch_transcript"
    try:
        # isTranscriptExist = await transcript_exists(video_id);
        # if isTranscriptExist:
        #     return isTranscriptExist.transcript;

        repository = TranscriptRepository()
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = "\n".join(
            [f"{item['start']:.2f}s: {item['text']}" for item in transcript]
        )

        await repository.save_transcript(video_id, transcript, transcript_text)
        print("end")
        return transcript
    except Exception as e:
        raise RuntimeError(f"{method_name} Failed to fetch transcript: {str(e)}")


async def get_transcript_row(video_id: str) -> TranscriptRow:
    """Fetches a transcript by video ID.

    Args:
        video_id (str): The ID of the video.

    Returns:
        TranscriptRow: The transcript record.

    Raises:
        RuntimeError: If fetching the transcript fails.
    """
    method_name = "transcript_service/get_transcript_row"
    try:
        repository = TranscriptRepository()
        transcript = await repository.get_transcript(video_id)
        if transcript:
            return transcript
        raise RuntimeError(
            f"{method_name} Transcript not found for video ID: {video_id}"
        )
    except Exception as e:
        raise RuntimeError(f"{method_name} Failed to fetch transcript: {str(e)}")


async def transcript_exists(video_id: str) -> bool:
    """Check if a transcript exists in the database.

    Args:
        video_id (str): The video ID.

    Returns:
        bool: True if the transcript exists, False otherwise.
    """
    method_name = "transcript_service/transcript_exists"
    try:
        repository = TranscriptRepository()
        transcript = await repository.get_transcript(video_id)

        if transcript:
            return True

        return False
    except Exception as e:
        raise RuntimeError(
            f"{method_name} Failed to check transcript existence: {str(e)}"
        )
