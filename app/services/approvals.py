import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.approval import Approval, ApprovalStatus
from app.models.task import Task
from app.schemas.approval import ApprovalCreate, ApprovalDecision
from app.schemas.audit import AuditCreate
from app.services.audits import add_audit


class ApprovalServiceError(ValueError):
    """Base error raised when an Approval business rule is violated."""


class ApprovalNotFoundError(ApprovalServiceError):
    pass


class InvalidApprovalReferenceError(ApprovalServiceError):
    pass


class InvalidApprovalDecisionError(ApprovalServiceError):
    pass


def list_approvals(
    session: Session,
    *,
    task_id: uuid.UUID | None = None,
    director_id: uuid.UUID | None = None,
    approval_status: ApprovalStatus | None = None,
) -> list[Approval]:
    statement = select(Approval)
    if task_id is not None:
        statement = statement.where(Approval.task_id == task_id)
    if director_id is not None:
        statement = statement.where(Approval.director_id == director_id)
    if approval_status is not None:
        statement = statement.where(Approval.status == approval_status)
    statement = statement.order_by(Approval.requested_at.desc(), Approval.id)
    return list(session.scalars(statement).all())


def require_approval(session: Session, approval_id: uuid.UUID) -> Approval:
    approval = session.get(Approval, approval_id)
    if approval is None:
        raise ApprovalNotFoundError(f"Approval '{approval_id}' was not found.")
    return approval


def create_approval(
    session: Session, task_id: uuid.UUID, payload: ApprovalCreate
) -> Approval:
    task = session.get(Task, task_id)
    if task is None:
        raise InvalidApprovalReferenceError("The Approval Task does not exist.")
    if task.director_id != payload.director_id:
        raise InvalidApprovalReferenceError(
            "The Approval Director must match the Task's owning Director."
        )

    approval = Approval(task_id=task_id, **payload.model_dump())
    session.add(approval)
    session.flush()
    add_audit(
        session,
        AuditCreate(
            director_id=payload.director_id,
            task_id=task_id,
            event_type="approval.requested",
            actor_type="system",
            entity_type="approval",
            entity_id=str(approval.id),
            details={"action": payload.action},
        ),
    )
    session.commit()
    session.refresh(approval)
    return approval


def decide_approval(
    session: Session, approval: Approval, payload: ApprovalDecision
) -> Approval:
    if approval.status != ApprovalStatus.PENDING:
        raise InvalidApprovalDecisionError("A decided Approval cannot be changed.")
    if payload.status == ApprovalStatus.PENDING:
        raise InvalidApprovalDecisionError("An Approval decision cannot return to pending.")

    approval.status = payload.status
    approval.reviewed_by = payload.reviewed_by
    approval.decision_notes = payload.decision_notes
    approval.decided_at = datetime.now(timezone.utc)
    add_audit(
        session,
        AuditCreate(
            director_id=approval.director_id,
            task_id=approval.task_id,
            event_type="approval.decided",
            actor_type="human",
            actor_id=payload.reviewed_by,
            entity_type="approval",
            entity_id=str(approval.id),
            details={"status": payload.status.value, "notes": payload.decision_notes},
        ),
    )
    session.commit()
    session.refresh(approval)
    return approval
