# app/repositories/analyze_repository.py

from typing import Optional
import psycopg2
from psycopg2 import Error
from app.core.config import settings
import json


class AnalyzeRepository:
    """
    Handles CRUD operations for analysis results.
    """

    def __init__(self):
        self.connection = psycopg2.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            dbname=settings.DB_NAME,
            port=settings.DB_PORT,
        )

    def save_analysis(self, video_id: str, analysis: dict) -> int:
        """
        Inserts an analysis result into the database.

        Args:
            video_id (str): The video ID associated with the analysis.
            analysis (dict): The analysis data to insert.

        Returns:
            int: The ID of the newly created analysis record.
        """
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO analysis_results (video_id, analysis)
            VALUES (%s, %s)
            RETURNING id
            """
            cursor.execute(query, (video_id, json.dumps(analysis)))
            self.connection.commit()
            analysis_id = cursor.fetchone()[0]
            return analysis_id
        except Error as e:
            print(f"Error saving analysis: {e}")
            raise
        finally:
            cursor.close()

    def get_analysis(self, analysis_id: int) -> Optional[dict]:
        """
        Fetches an analysis result by ID.

        Args:
            analysis_id (int): The ID of the analysis to fetch.

        Returns:
            Optional[dict]: The analysis data, or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM analysis_results WHERE id = %s"
            cursor.execute(query, (analysis_id,))
            record = cursor.fetchone()
            if record:
                record = dict(record)
                record["analysis"] = json.loads(record["analysis"])
                return record
            return None
        except Error as e:
            print(f"Error fetching analysis: {e}")
            raise
        finally:
            cursor.close()
