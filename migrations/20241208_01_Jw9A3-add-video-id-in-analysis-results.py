"""
add video id in analysis results
"""

from yoyo import step

__depends__ = {"20241202_03_AP7aC-add-constraint-in-video-id"}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE analysis_results
        ADD COLUMN video_id VARCHAR(50) NOT NULL
        """
    )


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE analysis_results
        DROP COLUMN video_id -- Drop video_id column
        """
    )


steps = [step(apply=apply_step, rollback=rollback_step)]
