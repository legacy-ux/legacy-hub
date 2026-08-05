import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class AuditCreate(BaseModel):
    director_id: uuid.UUID
    task_id: uuid.UUID | None = None
    event_type: str = Field(min_length=1, max_length=100)
    actor_type: str = Field(min_length=1, max_length=50)
    actor_id: str | None = Field(default=None, min_length=1, max_length=255)
    entity_type: str = Field(min_length=1, max_length=100)
    entity_id: str | None = Field(default=None, min_length=1, max_length=255)
    details: dict[str, Any] | None = None


class AuditRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    director_id: uuid.UUID
    task_id: uuid.UUID | None
    event_type: str
    actor_type: str
    actor_id: str | None
    entity_type: str
    entity_id: str | None
    details: dict[str, Any] | None
    created_at: datetime
