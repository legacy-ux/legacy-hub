from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from pydantic import BaseModel

from app.config import get_settings
from app.models.director import DirectorKey


class AuthenticatedPrincipal(BaseModel):
    """Verified caller identity supplied by the Legacy identity provider."""

    subject: str
    director_key: DirectorKey
    is_human: bool
    email: str | None = None


bearer_scheme = HTTPBearer(auto_error=False)


def get_current_principal(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
) -> AuthenticatedPrincipal:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="A valid bearer token is required.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    settings = get_settings()
    try:
        claims = jwt.decode(
            credentials.credentials,
            settings.auth_secret_key,
            algorithms=[settings.auth_algorithm],
            audience=settings.auth_audience,
            issuer=settings.auth_issuer,
            options={"require": ["sub", "director", "human", "exp", "iat"]},
        )
        if not isinstance(claims["human"], bool):
            raise ValueError("The human claim must be a boolean.")
        return AuthenticatedPrincipal(
            subject=claims["sub"],
            director_key=DirectorKey(claims["director"]),
            is_human=claims["human"],
            email=claims.get("email"),
        )
    except (InvalidTokenError, KeyError, TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The bearer token is invalid or expired.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
