from pydantic import BaseModel

from app.models.director import DirectorKey
from app.security.permissions import Permission
from app.security.approvals import ApprovalAction


class PrincipalRead(BaseModel):
    subject: str
    director_key: DirectorKey
    is_human: bool
    email: str | None
    permissions: list[Permission]


class PermissionMatrixRead(BaseModel):
    director_key: DirectorKey
    permissions: list[Permission]


class ApprovalMatrixRead(BaseModel):
    action: ApprovalAction
    eligible_reviewers: list[DirectorKey]
    human_required: bool = True
