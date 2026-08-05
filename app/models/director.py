import uuid
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, Enum, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.approval import Approval
    from app.models.message import Message
    from app.models.specialist import Specialist
    from app.models.task import Task


class DirectorKey(StrEnum):
    """Stable registry keys for the four Legacy v1 Director seats."""

    OWNER = "owner"
    DESIGN_SALES = "design_sales"
    ACCOUNT_MANAGER = "account_manager"
    CREW_LEADER = "crew_leader"


class Director(Base):
    """A seat-based Director responsible for a Legacy Hub business workflow."""

    __tablename__ = "directors"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    key: Mapped[DirectorKey] = mapped_column(
        Enum(DirectorKey, name="director_key", native_enum=False, length=32),
        unique=True,
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True, server_default="true"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    specialists: Mapped[list["Specialist"]] = relationship(back_populates="director")
    tasks: Mapped[list["Task"]] = relationship(back_populates="director")
    messages: Mapped[list["Message"]] = relationship(back_populates="director")
    approvals: Mapped[list["Approval"]] = relationship(back_populates="director")

    def __repr__(self) -> str:
        return f"Director(id={self.id!r}, key={self.key!r}, name={self.name!r})"
