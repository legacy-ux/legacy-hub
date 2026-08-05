"""Authentication and authorization primitives for Legacy Hub."""

from app.security.auth import AuthenticatedPrincipal, get_current_principal
from app.security.permissions import Permission, require_permission

__all__ = [
    "AuthenticatedPrincipal",
    "Permission",
    "get_current_principal",
    "require_permission",
]
