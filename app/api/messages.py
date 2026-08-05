import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.message import Message, MessageDirection
from app.schemas.message import MessageCreate, MessageRead
from app.services.messages import (
    InvalidMessageReferenceError,
    MessageNotFoundError,
    create_message,
    list_messages,
    require_message,
)
from app.security.permissions import Permission, require_permission


router = APIRouter(prefix="/api/v1/messages", tags=["messages"])
DatabaseSession = Annotated[Session, Depends(get_db)]


def _message_or_404(db: Session, message_id: uuid.UUID) -> Message:
    try:
        return require_message(db, message_id)
    except MessageNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "",
    response_model=list[MessageRead],
    dependencies=[Depends(require_permission(Permission.MESSAGE_READ))],
)
def read_messages(
    db: DatabaseSession,
    task_id: Annotated[uuid.UUID | None, Query()] = None,
    director_id: Annotated[uuid.UUID | None, Query()] = None,
    specialist_id: Annotated[uuid.UUID | None, Query()] = None,
    direction: Annotated[MessageDirection | None, Query()] = None,
    channel: Annotated[str | None, Query(max_length=50)] = None,
) -> list[MessageRead]:
    return list_messages(
        db,
        task_id=task_id,
        director_id=director_id,
        specialist_id=specialist_id,
        direction=direction,
        channel=channel,
    )


@router.post(
    "/tasks/{task_id}", response_model=MessageRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(Permission.MESSAGE_WRITE))],
)
def create_message_route(
    task_id: uuid.UUID, payload: MessageCreate, db: DatabaseSession
) -> MessageRead:
    try:
        return create_message(db, task_id, payload)
    except InvalidMessageReferenceError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/{message_id}",
    response_model=MessageRead,
    dependencies=[Depends(require_permission(Permission.MESSAGE_READ))],
)
def read_message(message_id: uuid.UUID, db: DatabaseSession) -> MessageRead:
    return _message_or_404(db, message_id)
