from fastapi import APIRouter


router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict[str, str]:
    """Return the service health status."""

    return {
        "status": "healthy",
        "service": "legacy-hub",
    }
