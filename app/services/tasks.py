import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.director import Director
from app.models.specialist import Specialist
from app.models.task import Task, TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate


class TaskEngineError(ValueError):
    """Base error raised when a Task Engine business rule is violated."""


class TaskNotFoundError(TaskEngineError):
    pass


class InvalidTaskReferenceError(TaskEngineError):
    pass


class InvalidTaskTransitionError(TaskEngineError):
    pass


ALLOWED_TRANSITIONS: dict[TaskStatus, frozenset[TaskStatus]] = {
    TaskStatus.PENDING: frozenset(
        {TaskStatus.IN_PROGRESS, TaskStatus.BLOCKED, TaskStatus.CANCELLED}
    ),
    TaskStatus.IN_PROGRESS: frozenset(
        {TaskStatus.BLOCKED, TaskStatus.COMPLETED, TaskStatus.CANCELLED}
    ),
    TaskStatus.BLOCKED: frozenset(
        {TaskStatus.PENDING, TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED}
    ),
    TaskStatus.COMPLETED: frozenset(),
    TaskStatus.CANCELLED: frozenset(),
}


def list_tasks(
    session: Session,
    *,
    director_id: uuid.UUID | None = None,
    specialist_id: uuid.UUID | None = None,
    task_status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
) -> list[Task]:
    statement = select(Task)
    if director_id is not None:
        statement = statement.where(Task.director_id == director_id)
    if specialist_id is not None:
        statement = statement.where(Task.specialist_id == specialist_id)
    if task_status is not None:
        statement = statement.where(Task.status == task_status)
    if priority is not None:
        statement = statement.where(Task.priority == priority)
    statement = statement.order_by(Task.created_at.desc(), Task.id)
    return list(session.scalars(statement).all())


def get_task(session: Session, task_id: uuid.UUID) -> Task | None:
    return session.get(Task, task_id)


def require_task(session: Session, task_id: uuid.UUID) -> Task:
    task = get_task(session, task_id)
    if task is None:
        raise TaskNotFoundError(f"Task '{task_id}' was not found.")
    return task


def _require_active_director(session: Session, director_id: uuid.UUID) -> Director:
    director = session.get(Director, director_id)
    if director is None or not director.is_active:
        raise InvalidTaskReferenceError("The owning Director does not exist or is inactive.")
    return director


def _validate_specialist(
    session: Session, specialist_id: uuid.UUID, director_id: uuid.UUID
) -> Specialist:
    specialist = session.get(Specialist, specialist_id)
    if specialist is None or not specialist.is_active:
        raise InvalidTaskReferenceError("The assigned Specialist does not exist or is inactive.")
    if specialist.director_id != director_id:
        raise InvalidTaskReferenceError(
            "The assigned Specialist must be supervised by the Task's owning Director."
        )
    return specialist


def create_task(session: Session, payload: TaskCreate) -> Task:
    _require_active_director(session, payload.director_id)
    if payload.specialist_id is not None:
        _validate_specialist(session, payload.specialist_id, payload.director_id)

    task = Task(**payload.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, task: Task, payload: TaskUpdate) -> Task:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    session.commit()
    session.refresh(task)
    return task


def assign_task(
    session: Session, task: Task, specialist_id: uuid.UUID | None
) -> Task:
    if task.status in {TaskStatus.COMPLETED, TaskStatus.CANCELLED}:
        raise InvalidTaskTransitionError("A terminal Task cannot be reassigned.")
    if specialist_id is not None:
        _validate_specialist(session, specialist_id, task.director_id)
    task.specialist_id = specialist_id
    session.commit()
    session.refresh(task)
    return task


def transition_task(session: Session, task: Task, new_status: TaskStatus) -> Task:
    if new_status == task.status:
        return task
    if new_status not in ALLOWED_TRANSITIONS[task.status]:
        raise InvalidTaskTransitionError(
            f"Task cannot transition from '{task.status}' to '{new_status}'."
        )

    task.status = new_status
    task.completed_at = (
        datetime.now(timezone.utc) if new_status == TaskStatus.COMPLETED else None
    )
    session.commit()
    session.refresh(task)
    return task
