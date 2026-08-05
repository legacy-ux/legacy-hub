from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.director import DirectorKey
from app.schemas.director import DirectorRead
from app.services.directors import get_director, list_directors, synchronize_directors
from app.security.permissions import Permission, require_permission


router = APIRouter(prefix="/api/v1/directors", tags=["directors"])
DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get(
    "",
    response_model=list[DirectorRead],
    dependencies=[Depends(require_permission(Permission.DIRECTOR_READ))],
)
def read_directors(
    db: DatabaseSession,
    active_only: Annotated[bool, Query()] = True,
) -> list[DirectorRead]:
    """List the registered Legacy Director seats."""

    return list_directors(db, active_only=active_only)


@router.get(
    "/{key}",
    response_model=DirectorRead,
    dependencies=[Depends(require_permission(Permission.DIRECTOR_READ))],
)
def read_director(key: DirectorKey, db: DatabaseSession) -> DirectorRead:
    """Return one Director seat by its stable key."""

    director = get_director(db, key)
    if director is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Director '{key}' was not found.",
        )
    return director


@router.post(
    "/actions/sync",
    response_model=list[DirectorRead],
    dependencies=[Depends(require_permission(Permission.DIRECTOR_SYNC))],
)
def sync_directors(db: DatabaseSession) -> list[DirectorRead]:
    """Synchronize the four authoritative Director seats idempotently."""

    return synchronize_directors(db)
