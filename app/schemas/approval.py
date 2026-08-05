import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.models.approval import ApprovalStatus
from app.security.approvals import ApprovalAction


class ApprovalCreate(BaseModel):
    director_id: uuid.UUID
    action: ApprovalAction
    request_details: str | None = None


class ApprovalDecision(BaseModel):
    status: ApprovalStatus
    decision_notes: str | None = None

    @model_validator(mode="after")
    def require_terminal_status(self) -> "ApprovalDecision":
        if self.status == ApprovalStatus.PENDING:
            raise ValueError("An approval decision cannot return to pending.")
        return self


class ApprovalRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    task_id: uuid.UUID
    director_id: uuid.UUID
    action: str
    request_details: str | None
    status: ApprovalStatus
    reviewed_by: str | None
    decision_notes: str | None
    requested_at: datetime
    decided_at: datetime | None
    updated_at: datetime
