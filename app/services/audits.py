import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.audit import Audit
from app.models.director import Director
from app.models.task import Task
from app.schemas.audit import AuditCreate


class AuditServiceError(ValueError):
    """Base error raised when an audit business rule is violated."""


class AuditNotFoundError(AuditServiceError):
    pass


class InvalidAuditReferenceError(AuditServiceError):
    pass


def list_audits(
    session: Session,
    *,
    director_id: uuid.UUID | None = None,
    task_id: uuid.UUID | None = None,
    event_type: str | None = None,
    entity_type: str | None = None,
    entity_id: str | None = None,
) -> list[Audit]:
    statement = select(Audit)
    if director_id is not None:
        statement = statement.where(Audit.director_id == director_id)
    if task_id is not None:
        statement = statement.where(Audit.task_id == task_id)
    if event_type is not None:
        statement = statement.where(Audit.event_type == event_type)
    if entity_type is not None:
        statement = statement.where(Audit.entity_type == entity_type)
    if entity_id is not None:
        statement = statement.where(Audit.entity_id == entity_id)
    statement = statement.order_by(Audit.created_at.desc(), Audit.id)
    return list(session.scalars(statement).all())


def require_audit(session: Session, audit_id: uuid.UUID) -> Audit:
    audit = session.get(Audit, audit_id)
    if audit is None:
        raise AuditNotFoundError(f"Audit '{audit_id}' was not found.")
    return audit


def _validate_audit_references(session: Session, payload: AuditCreate) -> None:
    director = session.get(Director, payload.director_id)
    if director is None:
        raise InvalidAuditReferenceError("The Audit Director does not exist.")
    if payload.task_id is None:
        return
    task = session.get(Task, payload.task_id)
    if task is None:
        raise InvalidAuditReferenceError("The Audit Task does not exist.")
    if task.director_id != payload.director_id:
        raise InvalidAuditReferenceError(
            "The Audit Director must match the Task's owning Director."
        )


def add_audit(session: Session, payload: AuditCreate) -> Audit:
    """Append an audit event without committing the surrounding transaction."""

    _validate_audit_references(session, payload)
    audit = Audit(**payload.model_dump())
    session.add(audit)
    session.flush()
    return audit


def create_audit(session: Session, payload: AuditCreate) -> Audit:
    audit = add_audit(session, payload)
    session.commit()
    session.refresh(audit)
    return audit
