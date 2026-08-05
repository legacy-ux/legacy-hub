from enum import StrEnum

from app.models.director import DirectorKey
from app.security.auth import AuthenticatedPrincipal


class ApprovalAction(StrEnum):
    CUSTOMER_DOCUMENT_FIRST_SEND = "customer_document.first_send"
    CUSTOMER_DOCUMENT_REVISION_SEND = "customer_document.revision_send"
    HIGH_VALUE_OR_COMPLEX_PROPOSAL = "proposal.high_value_or_complex"
    FINANCIAL_TRANSACTION = "financial.transaction"
    OWNER_OVERRIDE = "owner.override"


APPROVAL_REVIEWERS: dict[ApprovalAction, frozenset[DirectorKey]] = {
    ApprovalAction.CUSTOMER_DOCUMENT_FIRST_SEND: frozenset(
        {DirectorKey.OWNER, DirectorKey.DESIGN_SALES, DirectorKey.ACCOUNT_MANAGER}
    ),
    ApprovalAction.CUSTOMER_DOCUMENT_REVISION_SEND: frozenset(
        {DirectorKey.OWNER, DirectorKey.DESIGN_SALES, DirectorKey.ACCOUNT_MANAGER}
    ),
    ApprovalAction.HIGH_VALUE_OR_COMPLEX_PROPOSAL: frozenset({DirectorKey.OWNER}),
    ApprovalAction.FINANCIAL_TRANSACTION: frozenset({DirectorKey.OWNER}),
    ApprovalAction.OWNER_OVERRIDE: frozenset({DirectorKey.OWNER}),
}


def can_decide_approval(
    principal: AuthenticatedPrincipal, action: ApprovalAction
) -> bool:
    return principal.is_human and principal.director_key in APPROVAL_REVIEWERS[action]
