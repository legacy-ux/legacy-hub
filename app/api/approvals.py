import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.approval import Approval, ApprovalStatus
from app.schemas.approval import ApprovalCreate, ApprovalDecision, ApprovalRead
from app.services.approvals import (
    ApprovalPermissionError,
    ApprovalNotFoundError,
    InvalidApprovalDecisionError,
    InvalidApprovalReferenceError,
    create_approval,
    decide_approval,
    list_approvals,
    require_approval,
)
from app.security.auth import AuthenticatedPrincipal
from app.security.permissions import Permission, require_permission


router = APIRouter(prefix="/api/v1/approvals", tags=["approvals"])
DatabaseSession = Annotated[Session, Depends(get_db)]
Principal = Annotated[
    AuthenticatedPrincipal,
    Depends(require_permission(Permission.APPROVAL_DECIDE)),
]


def _approval_or_404(db: Session, approval_id: uuid.UUID) -> Approval:
    try:
        return require_approval(db, approval_id)
    except ApprovalNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "",
    response_model=list[ApprovalRead],
    dependencies=[Depends(require_permission(Permission.APPROVAL_READ))],
)
def read_approvals(
    db: DatabaseSession,
    task_id: Annotated[uuid.UUID | None, Query()] = None,
    director_id: Annotated[uuid.UUID | None, Query()] = None,
    approval_status: Annotated[ApprovalStatus | None, Query(alias="status")] = None,
) -> list[ApprovalRead]:
    return list_approvals(
        db,
        task_id=task_id,
        director_id=director_id,
        approval_status=approval_status,
    )


@router.post(
    "/tasks/{task_id}", response_model=ApprovalRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(Permission.APPROVAL_REQUEST))],
)
def create_approval_route(
    task_id: uuid.UUID, payload: ApprovalCreate, db: DatabaseSession
) -> ApprovalRead:
    try:
        return create_approval(db, task_id, payload)
    except InvalidApprovalReferenceError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/{approval_id}",
    response_model=ApprovalRead,
    dependencies=[Depends(require_permission(Permission.APPROVAL_READ))],
)
def read_approval(approval_id: uuid.UUID, db: DatabaseSession) -> ApprovalRead:
    return _approval_or_404(db, approval_id)


@router.post("/{approval_id}/actions/decide", response_model=ApprovalRead)
def decide_approval_route(
    approval_id: uuid.UUID, payload: ApprovalDecision, db: DatabaseSession, principal: Principal
) -> ApprovalRead:
    try:
        return decide_approval(db, _approval_or_404(db, approval_id), payload, principal)
    except ApprovalPermissionError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except InvalidApprovalDecisionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
