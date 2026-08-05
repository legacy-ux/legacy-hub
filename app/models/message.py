import uuid
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.director import Director
    from app.models.specialist import Specialist
    from app.models.task import Task


class MessageDirection(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    INTERNAL = "internal"
    SYSTEM = "system"


class Message(Base):
    """A communication record associated with a Legacy Hub task."""

    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    task_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True
    )
    director_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("directors.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    specialist_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("specialists.id", ondelete="SET NULL"), nullable=True, index=True
    )
    direction: Mapped[MessageDirection] = mapped_column(
        Enum(MessageDirection, name="message_direction", native_enum=False, length=16),
        nullable=False,
        default=MessageDirection.INTERNAL,
        server_default=MessageDirection.INTERNAL.value,
        index=True,
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    channel: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
    external_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), index=True
    )

    task: Mapped["Task"] = relationship(back_populates="messages")
    director: Mapped["Director"] = relationship(back_populates="messages")
    specialist: Mapped["Specialist | None"] = relationship(back_populates="messages")

    def __repr__(self) -> str:
        return (
            f"Message(id={self.id!r}, task_id={self.task_id!r}, "
            f"direction={self.direction!r})"
        )
