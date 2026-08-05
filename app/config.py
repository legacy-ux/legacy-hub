from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Legacy Hub"
    environment: str = "development"
    debug: bool = False
    api_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://legacy:legacy@db:5432/legacy_hub"
    auth_secret_key: str = "change-me-before-production-with-a-secure-secret"
    auth_algorithm: str = "HS256"
    auth_issuer: str = "legacy-hub"
    auth_audience: str = "legacy-hub-api"

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
