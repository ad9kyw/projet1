from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration for app, load from .env file"""
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()