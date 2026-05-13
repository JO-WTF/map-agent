from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "map-agent-backend"
    redis_url: str = "redis://localhost:6379/0"
    storage_dir: str = "./data"


settings = Settings()
