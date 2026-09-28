from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "Modern Interactive Learning Platform"
    API_V1_STR: str = "/api"
    ENVIRONMENT: str = "development"
    PORT: int = 8000

    # MongoDB
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "learning_platform"

    # Clerk Auth
    CLERK_SECRET_KEY: str = ""
    CLERK_ISSUER: str = ""
    CLERK_JWKS_URL: str = ""

    # CORS
    FRONTEND_URL: str = "http://localhost:3000"
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
    ]

    model_config = SettingsConfigDict(
        env_file=(".env", "backend/.env", "../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> List[str]:
        origins = set(self.CORS_ORIGINS)
        if self.FRONTEND_URL:
            origins.add(self.FRONTEND_URL.rstrip("/"))
        return list(origins)


settings = Settings()
