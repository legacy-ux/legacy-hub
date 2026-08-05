import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.task import TaskPriority, TaskStatus
from app.schemas.task import TaskAssignment, TaskCreate, TaskRead, TaskTransition, TaskUpdate
from app.services.tasks import (
    InvalidTaskReferenceError,
    InvalidTaskTransitionError,
    TaskNotFoundError,
    assign_task,
    create_task,
    list_tasks,
    require_task,
    transition_task,
    update_task,
)
from app.security.permissions import Permission, require_permission


router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])
DatabaseSession = Annotated[Session, Depends(get_db)]


def _task_or_404(db: Session, task_id: uuid.UUID):
    try:
        return require_task(db, task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


def _raise_rule_error(exc: ValueError) -> None:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "",
    response_model=list[TaskRead],
    dependencies=[Depends(require_permission(Permission.TASK_READ))],
)
def read_tasks(
    db: DatabaseSession,
    director_id: Annotated[uuid.UUID | None, Query()] = None,
    specialist_id: Annotated[uuid.UUID | None, Query()] = None,
    task_status: Annotated[TaskStatus | None, Query(alias="status")] = None,
    priority: Annotated[TaskPriority | None, Query()] = None,
) -> list[TaskRead]:
    return list_tasks(
        db,
        director_id=director_id,
        specialist_id=specialist_id,
        task_status=task_status,
        priority=priority,
    )


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(Permission.TASK_WRITE))],
)
def create_task_route(payload: TaskCreate, db: DatabaseSession) -> TaskRead:
    try:
        return create_task(db, payload)
    except InvalidTaskReferenceError as exc:
        _raise_rule_error(exc)


@router.get(
    "/{task_id}",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(Permission.TASK_READ))],
)
def read_task(task_id: uuid.UUID, db: DatabaseSession) -> TaskRead:
    return _task_or_404(db, task_id)


@router.patch(
    "/{task_id}",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(Permission.TASK_WRITE))],
)
def update_task_route(
    task_id: uuid.UUID, payload: TaskUpdate, db: DatabaseSession
) -> TaskRead:
    return update_task(db, _task_or_404(db, task_id), payload)


@router.post(
    "/{task_id}/actions/assign",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(Permission.TASK_WRITE))],
)
def assign_task_route(
    task_id: uuid.UUID, payload: TaskAssignment, db: DatabaseSession
) -> TaskRead:
    try:
        return assign_task(db, _task_or_404(db, task_id), payload.specialist_id)
    except (InvalidTaskReferenceError, InvalidTaskTransitionError) as exc:
        _raise_rule_error(exc)


@router.post(
    "/{task_id}/actions/transition",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(Permission.TASK_WRITE))],
)
def transition_task_route(
    task_id: uuid.UUID, payload: TaskTransition, db: DatabaseSession
) -> TaskRead:
    try:
        return transition_task(db, _task_or_404(db, task_id), payload.status)
    except InvalidTaskTransitionError as exc:
        _raise_rule_error(exc)
