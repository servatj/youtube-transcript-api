# app/repositories/transcript_repository.py

from typing import List, Optional
from mysql.connector import connect, Error
from app.core.config import settings
from app.models.transcript import Transcript
import json

class TranscriptRepository:
    """
    Handles CRUD operations for transcripts.
    """

    def __init__(self):
        self.connection = connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
            port=settings.DB_PORT,
        )

    def create_transcript(self, transcript: Transcript) -> int:
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
            INSERT INTO analyses (video_id, transcript, analysis)
            VALUES (%s, %s, %s)
            """
            cursor.execute(
                query,
                (transcript.video_id, transcript.transcript, json.dumps(transcript.analysis))
            )
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating transcript: {e}")
            raise
        finally:
            cursor.close()

    def get_transcript(self, transcript_id: int) -> Optional[Transcript]:
        """
        Fetches a transcript by ID.

        Args:
            transcript_id (int): The ID of the transcript to fetch.

        Returns:
            Optional[Transcript]: The transcript record, or None if not found.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM analyses WHERE id = %s"
            cursor.execute(query, (transcript_id,))
            record = cursor.fetchone()
            if record:
                record["analysis"] = json.loads(record["analysis"])
                return Transcript(**record)
            return None
        except Error as e:
            print(f"Error fetching transcript: {e}")
            raise
        finally:
            cursor.close()

    # Add additional CRUD methods (update, delete) if needed.