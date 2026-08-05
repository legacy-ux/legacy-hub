import uuid
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.director import Director
    from app.models.message import Message
    from app.models.task import Task


class SpecialistKey(StrEnum):
    """Stable registry keys for the four Legacy v1 specialist agents."""

    PLANT_LIBRARY = "plant_library"
    RESEARCH = "research"
    DESIGN = "design"
    FINANCIAL_ANALYSIS = "financial_analysis"


class Specialist(Base):
    """A bounded specialist agent supervised by a seat-based Director."""

    __tablename__ = "specialists"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    director_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("directors.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    key: Mapped[SpecialistKey] = mapped_column(
        Enum(SpecialistKey, name="specialist_key", native_enum=False, length=32),
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

    director: Mapped["Director"] = relationship(back_populates="specialists")
    tasks: Mapped[list["Task"]] = relationship(back_populates="specialist")
    messages: Mapped[list["Message"]] = relationship(back_populates="specialist")

    def __repr__(self) -> str:
        return f"Specialist(id={self.id!r}, key={self.key!r}, name={self.name!r})"
