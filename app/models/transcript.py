from pydantic import BaseModel
from typing import List


class TranscriptItem(BaseModel):
    video_id: str
    text: str
    start: float
    duration: float


class TranscriptRequest(BaseModel):
    transcript: List[TranscriptItem]
