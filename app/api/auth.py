from typing import Annotated

from fastapi import APIRouter, Depends

from app.models.director import DirectorKey
from app.schemas.auth import ApprovalMatrixRead, PermissionMatrixRead, PrincipalRead
from app.security.approvals import APPROVAL_REVIEWERS
from app.security.auth import AuthenticatedPrincipal, get_current_principal
from app.security.permissions import PERMISSION_MATRIX, Permission, require_permission


router = APIRouter(prefix="/api/v1/auth", tags=["authentication"])
Principal = Annotated[AuthenticatedPrincipal, Depends(get_current_principal)]


@router.get("/me", response_model=PrincipalRead)
def read_current_principal(principal: Principal) -> PrincipalRead:
    return PrincipalRead(
        **principal.model_dump(),
        permissions=sorted(PERMISSION_MATRIX[principal.director_key], key=str),
    )


@router.get(
    "/permissions",
    response_model=list[PermissionMatrixRead],
    dependencies=[Depends(require_permission(Permission.DIRECTOR_READ))],
)
def read_permission_matrix() -> list[PermissionMatrixRead]:
    return [
        PermissionMatrixRead(
            director_key=director_key,
            permissions=sorted(permissions, key=str),
        )
        for director_key, permissions in PERMISSION_MATRIX.items()
    ]


@router.get(
    "/approval-matrix",
    response_model=list[ApprovalMatrixRead],
    dependencies=[Depends(require_permission(Permission.APPROVAL_READ))],
)
def read_approval_matrix() -> list[ApprovalMatrixRead]:
    return [
        ApprovalMatrixRead(
            action=action,
            eligible_reviewers=sorted(reviewers, key=str),
        )
        for action, reviewers in APPROVAL_REVIEWERS.items()
    ]
