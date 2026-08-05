from fastapi import FastAPI

from app.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
)


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    """Return basic service metadata."""

    return {
        "service": "legacy-hub",
        "status": "running",
        "environment": settings.environment,
    }
