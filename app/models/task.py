import uuid
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.approval import Approval
    from app.models.audit import Audit
    from app.models.director import Director
    from app.models.message import Message
    from app.models.specialist import Specialist


class TaskStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(StrEnum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    director_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("directors.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    specialist_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("specialists.id", ondelete="SET NULL"), nullable=True, index=True
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status", native_enum=False, length=32),
        nullable=False,
        default=TaskStatus.PENDING,
        server_default=TaskStatus.PENDING.value,
        index=True,
    )
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority, name="task_priority", native_enum=False, length=16),
        nullable=False,
        default=TaskPriority.NORMAL,
        server_default=TaskPriority.NORMAL.value,
        index=True,
    )
    due_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    director: Mapped["Director"] = relationship(back_populates="tasks")
    specialist: Mapped["Specialist | None"] = relationship(back_populates="tasks")
    messages: Mapped[list["Message"]] = relationship(
        back_populates="task", cascade="all, delete-orphan"
    )
    approvals: Mapped[list["Approval"]] = relationship(
        back_populates="task", cascade="all, delete-orphan"
    )
    audits: Mapped[list["Audit"]] = relationship(back_populates="task")

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, status={self.status!r})"
