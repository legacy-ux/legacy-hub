import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.message import Message, MessageDirection
from app.models.specialist import Specialist
from app.models.task import Task
from app.schemas.audit import AuditCreate
from app.schemas.message import MessageCreate
from app.services.audits import add_audit


class MessageServiceError(ValueError):
    """Base error raised when a Message business rule is violated."""


class MessageNotFoundError(MessageServiceError):
    pass


class InvalidMessageReferenceError(MessageServiceError):
    pass


def list_messages(
    session: Session,
    *,
    task_id: uuid.UUID | None = None,
    director_id: uuid.UUID | None = None,
    specialist_id: uuid.UUID | None = None,
    direction: MessageDirection | None = None,
    channel: str | None = None,
) -> list[Message]:
    statement = select(Message)
    if task_id is not None:
        statement = statement.where(Message.task_id == task_id)
    if director_id is not None:
        statement = statement.where(Message.director_id == director_id)
    if specialist_id is not None:
        statement = statement.where(Message.specialist_id == specialist_id)
    if direction is not None:
        statement = statement.where(Message.direction == direction)
    if channel is not None:
        statement = statement.where(Message.channel == channel)
    statement = statement.order_by(Message.created_at.desc(), Message.id)
    return list(session.scalars(statement).all())


def require_message(session: Session, message_id: uuid.UUID) -> Message:
    message = session.get(Message, message_id)
    if message is None:
        raise MessageNotFoundError(f"Message '{message_id}' was not found.")
    return message


def _validate_message_context(
    session: Session, task_id: uuid.UUID, payload: MessageCreate
) -> Task:
    task = session.get(Task, task_id)
    if task is None:
        raise InvalidMessageReferenceError("The Message Task does not exist.")
    if task.director_id != payload.director_id:
        raise InvalidMessageReferenceError(
            "The Message Director must match the Task's owning Director."
        )
    if payload.specialist_id is not None:
        specialist = session.get(Specialist, payload.specialist_id)
        if specialist is None or not specialist.is_active:
            raise InvalidMessageReferenceError(
                "The Message Specialist does not exist or is inactive."
            )
        if specialist.director_id != task.director_id:
            raise InvalidMessageReferenceError(
                "The Message Specialist must be supervised by the Task's Director."
            )
    return task


def create_message(
    session: Session, task_id: uuid.UUID, payload: MessageCreate
) -> Message:
    _validate_message_context(session, task_id, payload)
    message = Message(task_id=task_id, **payload.model_dump())
    session.add(message)
    session.flush()
    add_audit(
        session,
        AuditCreate(
            director_id=payload.director_id,
            task_id=task_id,
            event_type="message.created",
            actor_type="system",
            entity_type="message",
            entity_id=str(message.id),
            details={"direction": payload.direction.value, "channel": payload.channel},
        ),
    )
    session.commit()
    session.refresh(message)
    return message
