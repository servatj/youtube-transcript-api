# app/repositories/transcript_repository.py

from typing import List, Optional
import psycopg2
from psycopg2 import sql, Error
from app.core.config import settings
from app.models.transcript import TranscriptItem
import json


class TranscriptRepository:
    """
    Handles CRUD operations for transcripts.
    """

    def __init__(self):
        self.connection = psycopg2.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            dbname=settings.DB_NAME,
            port=settings.DB_PORT,
        )

    def save_transcript(self, transcript: TranscriptItem) -> int:
        """
        Inserts a transcript into the database.

        Args:
          transcript (Transcript): The transcript to insert.

        Returns:
          int: The ID of the newly created transcript.
        """
        try:
            cursor = self.connection.cursor()
            query = """
      INSERT INTO analyses (video_id, transcript)
      VALUES (%s, %s, %s)
      RETURNING id
      """
            cursor.execute(
                query,
                (
                    transcript.video_id,
                    transcript.transcript,
                    json.dumps(transcript.analysis),
                ),
            )
            self.connection.commit()
            transcript_id = cursor.fetchone()[0]
            return transcript_id
        except Error as e:
            print(f"Error creating transcript: {e}")
            raise
        finally:
            cursor.close()

    def get_transcript(self, transcript_id: int) -> Optional[TranscriptItem]:
        """
        Fetches a transcript by ID.

        Args:
          transcript_id (int): The ID of the transcript to fetch.

        Returns:
          Optional[Transcript]: The transcript record, or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM analyses WHERE id = %s"
            cursor.execute(query, (transcript_id,))
            record = cursor.fetchone()
            if record:
                record = dict(zip([desc[0] for desc in cursor.description], record))
                record["analysis"] = json.loads(record["analysis"])
                return Transcript(**record)
            return None
        except Error as e:
            print(f"Error fetching transcript: {e}")
            raise
        finally:
            cursor.close()
