from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    redis_host: str
    redis_port: int
    queue_name: str
    worker_name: str
    retry_count: int
    retry_delay: float
    log_level: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()