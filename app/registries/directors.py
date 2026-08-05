from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.director import Director, DirectorKey


@dataclass(frozen=True, slots=True)
class DirectorDefinition:
    key: DirectorKey
    name: str
    description: str


DIRECTOR_REGISTRY: tuple[DirectorDefinition, ...] = (
    DirectorDefinition(
        DirectorKey.OWNER,
        "Owner Director",
        "Provides company-wide visibility, decisions, priorities, and executive oversight.",
    ),
    DirectorDefinition(
        DirectorKey.DESIGN_SALES,
        "Design & Sales Director",
        "Owns design, consultation, proposal, sales follow-up, and customer presentation workflows.",
    ),
    DirectorDefinition(
        DirectorKey.ACCOUNT_MANAGER,
        "Account Manager Director",
        "Owns property evaluations, customer care, maintenance exceptions, and enhancement opportunities.",
    ),
    DirectorDefinition(
        DirectorKey.CREW_LEADER,
        "Crew Leader Director",
        "Owns field execution, daily reporting, project documentation, issues, and completion updates.",
    ),
)


def sync_director_registry(session: Session) -> list[Director]:
    """Create or refresh the four fixed Director seats without duplicating rows."""

    existing = {
        director.key: director
        for director in session.scalars(select(Director)).all()
    }
    directors: list[Director] = []

    for definition in DIRECTOR_REGISTRY:
        director = existing.get(definition.key)
        if director is None:
            director = Director(key=definition.key, name=definition.name)
            session.add(director)

        director.name = definition.name
        director.description = definition.description
        director.is_active = True
        directors.append(director)

    session.commit()
    for director in directors:
        session.refresh(director)
    return directors
