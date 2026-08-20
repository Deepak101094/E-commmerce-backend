from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "E-Commerce AI Platform"
    APP_ENV: Environment = Environment.DEVELOPMENT
    APP_VERSION: str = "0.1.0"

    # API
    API_V1_PREFIX: str = "/api/v1"

    #DATABASE
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()