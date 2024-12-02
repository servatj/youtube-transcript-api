from typing import List

from pydantic import BaseModel


class TranscriptItem(BaseModel):
    text: str
    start: float
    duration: float


class TranscriptRequest(BaseModel):
    transcript: List[TranscriptItem]


class TranscriptYoutubeResponse(BaseModel):
    video_id: str
    transcript: List[TranscriptItem]


class TranscriptInsert(BaseModel):
    video_id: str
    transcript: List[TranscriptItem]
    transcript_json: dict
    transcript_length: int


class TranscriptRow(BaseModel):
    id: int
    video_id: str
    transcript: List[TranscriptItem]
    transcript_json: dict
    created_at: str
