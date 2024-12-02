"""
Create transcripts table
"""

from yoyo import step


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE transcripts (
                id SERIAL PRIMARY KEY,          -- Unique ID for the transcript
                video_id VARCHAR(255) NOT NULL, -- YouTube video ID
                transcript TEXT NOT NULL,       -- Transcript text
                transcript_json JSONB NOT NULL, -- Transcript JSON data
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of creation
            )
        """
    )
    # cursor.close()


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE transcripts")
    # cursor.close()


steps = [step(apply=apply_step, rollback=rollback_step)]
