from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "change-me-in-prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    DATABASE_URL: str = "sqlite:///./contacts.db"

    class Config:
        env_file = ".env"


settings = Settings()
