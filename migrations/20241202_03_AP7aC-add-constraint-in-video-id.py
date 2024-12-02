"""
add constraint in video id
"""

from yoyo import step

__depends__ = {"20241202_02_BobK2-add-new-table-analyse"}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE transcripts
        ADD CONSTRAINT unique_video_id UNIQUE (video_id);
        """
    )
    # cursor.close()


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE transcripts
        DROP CONSTRAINT unique_video_id;
        """
    )
    # cursor.close()


steps = [step(apply=apply_step, rollback=rollback_step)]
