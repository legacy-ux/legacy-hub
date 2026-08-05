from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.director import Director, DirectorKey
from app.registries.directors import sync_director_registry


def list_directors(session: Session, *, active_only: bool = True) -> list[Director]:
    """Return Director seats in a deterministic display order."""

    statement = select(Director)
    if active_only:
        statement = statement.where(Director.is_active.is_(True))
    statement = statement.order_by(Director.name)
    return list(session.scalars(statement).all())


def get_director(session: Session, key: DirectorKey) -> Director | None:
    """Return one Director seat by its stable registry key."""

    return session.scalar(select(Director).where(Director.key == key))


def synchronize_directors(session: Session) -> list[Director]:
    """Synchronize the database with the authoritative Director Registry."""

    return sync_director_registry(session)
