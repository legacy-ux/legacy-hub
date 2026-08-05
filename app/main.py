from fastapi import FastAPI

from app.api.directors import router as directors_router
from app.api.health import router as health_router
from app.api.tasks import router as tasks_router
from app.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(directors_router)
app.include_router(tasks_router)


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    """Return basic service metadata."""

    return {
        "service": "legacy-hub",
        "status": "running",
        "environment": settings.environment,
    }
