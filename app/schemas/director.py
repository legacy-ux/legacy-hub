import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.director import DirectorKey


class DirectorRead(BaseModel):
    """Public representation of a registered Director seat."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    key: DirectorKey
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime
