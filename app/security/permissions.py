from enum import StrEnum
from typing import Annotated, Callable

from fastapi import Depends, HTTPException, status

from app.models.director import DirectorKey
from app.security.auth import AuthenticatedPrincipal, get_current_principal


class Permission(StrEnum):
    DIRECTOR_READ = "director.read"
    DIRECTOR_SYNC = "director.sync"
    TASK_READ = "task.read"
    TASK_WRITE = "task.write"
    MESSAGE_READ = "message.read"
    MESSAGE_WRITE = "message.write"
    APPROVAL_READ = "approval.read"
    APPROVAL_REQUEST = "approval.request"
    APPROVAL_DECIDE = "approval.decide"
    AUDIT_READ = "audit.read"
    AUDIT_WRITE = "audit.write"


READ_PERMISSIONS = {
    Permission.DIRECTOR_READ,
    Permission.TASK_READ,
    Permission.MESSAGE_READ,
    Permission.APPROVAL_READ,
    Permission.AUDIT_READ,
}

PERMISSION_MATRIX: dict[DirectorKey, frozenset[Permission]] = {
    DirectorKey.OWNER: frozenset(Permission),
    DirectorKey.DESIGN_SALES: frozenset(
        READ_PERMISSIONS
        | {
            Permission.TASK_WRITE,
            Permission.MESSAGE_WRITE,
            Permission.APPROVAL_REQUEST,
            Permission.APPROVAL_DECIDE,
        }
    ),
    DirectorKey.ACCOUNT_MANAGER: frozenset(
        READ_PERMISSIONS
        | {
            Permission.TASK_WRITE,
            Permission.MESSAGE_WRITE,
            Permission.APPROVAL_REQUEST,
            Permission.APPROVAL_DECIDE,
        }
    ),
    DirectorKey.CREW_LEADER: frozenset(
        READ_PERMISSIONS
        | {
            Permission.TASK_WRITE,
            Permission.MESSAGE_WRITE,
            Permission.APPROVAL_REQUEST,
        }
    ),
}


def has_permission(principal: AuthenticatedPrincipal, permission: Permission) -> bool:
    return permission in PERMISSION_MATRIX[principal.director_key]


def require_permission(
    permission: Permission,
) -> Callable[..., AuthenticatedPrincipal]:
    def dependency(
        principal: Annotated[AuthenticatedPrincipal, Depends(get_current_principal)],
    ) -> AuthenticatedPrincipal:
        if not has_permission(principal, permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Director seat lacks permission '{permission.value}'.",
            )
        return principal

    return dependency
