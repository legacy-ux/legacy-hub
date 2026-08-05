from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed Legacy Hub settings."""

    app_name: str = "Legacy Hub"
    environment: str = "development"
    debug: bool = False
    api_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://legacy:legacy@db:5432/legacy_hub"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
