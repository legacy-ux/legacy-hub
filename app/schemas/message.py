import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.message import MessageDirection


class MessageCreate(BaseModel):
    director_id: uuid.UUID
    specialist_id: uuid.UUID | None = None
    direction: MessageDirection = MessageDirection.INTERNAL
    content: str = Field(min_length=1)
    channel: str | None = Field(default=None, min_length=1, max_length=50)
    external_id: str | None = Field(default=None, min_length=1, max_length=255)


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    task_id: uuid.UUID
    director_id: uuid.UUID
    specialist_id: uuid.UUID | None
    direction: MessageDirection
    content: str
    channel: str | None
    external_id: str | None
    created_at: datetime
