import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.audit import Audit
from app.schemas.audit import AuditCreate, AuditRead
from app.services.audits import (
    AuditNotFoundError,
    InvalidAuditReferenceError,
    create_audit,
    list_audits,
    require_audit,
)


router = APIRouter(prefix="/api/v1/audits", tags=["audits"])
DatabaseSession = Annotated[Session, Depends(get_db)]


def _audit_or_404(db: Session, audit_id: uuid.UUID) -> Audit:
    try:
        return require_audit(db, audit_id)
    except AuditNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("", response_model=list[AuditRead])
def read_audits(
    db: DatabaseSession,
    director_id: Annotated[uuid.UUID | None, Query()] = None,
    task_id: Annotated[uuid.UUID | None, Query()] = None,
    event_type: Annotated[str | None, Query(max_length=100)] = None,
    entity_type: Annotated[str | None, Query(max_length=100)] = None,
    entity_id: Annotated[str | None, Query(max_length=255)] = None,
) -> list[AuditRead]:
    return list_audits(
        db,
        director_id=director_id,
        task_id=task_id,
        event_type=event_type,
        entity_type=entity_type,
        entity_id=entity_id,
    )


@router.post("", response_model=AuditRead, status_code=status.HTTP_201_CREATED)
def create_audit_route(payload: AuditCreate, db: DatabaseSession) -> AuditRead:
    try:
        return create_audit(db, payload)
    except InvalidAuditReferenceError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get("/{audit_id}", response_model=AuditRead)
def read_audit(audit_id: uuid.UUID, db: DatabaseSession) -> AuditRead:
    return _audit_or_404(db, audit_id)
