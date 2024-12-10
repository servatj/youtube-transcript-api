"""
add analysis type to analysis results
"""

from yoyo import step

__depends__ = {"20241208_01_Jw9A3-add-video-id-in-analysis-results"}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE analysis_results
        ADD COLUMN analysis_type VARCHAR(100) NOT NULL DEFAULT 'general'; -- Add analysis_type with a default value
        """
    )
    # cursor.close()


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE analysis_results
        DROP COLUMN analysis_type; -- Drop the analysis_type column
        """
    )
    # cursor.close()


steps = [step(apply=apply_step, rollback=rollback_step)]
