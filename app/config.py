from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuration for app, load from .env file"""
    database_uri: str
    class Config:
        env_file = ".env"

settings = Settings()