"""
add new table analyse
"""

from yoyo import step

__depends__ = {"20241202_01_Iy3Be-create-transcripts-table"}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE analysis_results (
                id SERIAL PRIMARY KEY,           -- Unique ID for the analysis result
                transcript_id INT NOT NULL,      -- Foreign key referencing transcripts
                analysis JSONB NOT NULL,         -- Analysis result in JSON format
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
                FOREIGN KEY (transcript_id) REFERENCES transcripts(id) ON DELETE CASCADE -- Link to transcripts
            )
        """
    )
    # cursor.close()


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE analysis_results")
    # cursor.close()


[step(apply=apply_step, rollback=rollback_step)]
