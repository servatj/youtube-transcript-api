# app/repositories/transcript_repository.py

import json
from typing import Optional

from psycopg2.extensions import connection
from psycopg2 import Error

from app.models.transcript import TranscriptRow, TranscriptYoutubeResponse


class TranscriptRepository:
    """
    Handles CRUD operations for transcripts.
    """

    def __init__(self, db_client: connection):
        """
        Initializes the repository with a database client.

        Args:
          db_client (connection): A Psycopg2 database connection.
        """
        self.connection = db_client

    async def save_transcript(
        self, video_id, transcript: TranscriptYoutubeResponse, transcript_text: str
    ) -> int:
        """
        Inserts a transcript into the database.

        Args:
          transcript (Transcript): The transcript to insert.

        Returns:
          int: The ID of the newly created transcript.
        """
        method_name = "transcript_repository/save_transcript"
        print(f"{method_name} Saving transcript: {transcript} - start")
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO transcripts (video_id, transcript, transcript_json)
                VALUES (%s, %s, %s)
                RETURNING id
                """
            cursor.execute(
                query,
                (video_id, transcript_text, json.dumps(transcript)),
            )
            self.connection.commit()
            transcript_id = cursor.fetchone()[0]
            print(f"{method_name} - end Transcript saved with ID: {transcript_id}")
            return transcript_id
        except Error as e:
            print(f"Error creating transcript: {e}")
            raise
        finally:
            cursor.close()

    async def get_transcript(self, transcript_id: str) -> Optional[TranscriptRow]:
        """
        Fetches a transcript by ID.

        Args:
          transcript_id (int): The ID of the transcript to fetch.

        Returns:
          Optional[Transcript]: The transcript record, or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM transcripts WHERE video_id = %s"
            cursor.execute(query, (transcript_id,))
            record = cursor.fetchone()
            if record:
                return record
            return None
        except Error as e:
            print(f"Error fetching transcript: {e}")
            raise
        finally:
            print("Closing cursor")
            cursor.close()

    async def get_transcript_by_video_id(
        self, video_id: str
    ) -> Optional[TranscriptRow]:
        """
        Fetches a transcript by video ID.

        Args:
          video_id (str): The video ID of the transcript to fetch.

        Returns:
          Optional[Transcript]: The transcript record, or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM transcripts WHERE video_id = %s"
            cursor.execute(query, (video_id,))
            record = cursor.fetchone()
            if record:
                return record
            return None
        except Error as e:
            print(f"Error fetching transcript: {e}")
            raise
        finally:
            cursor.close()
