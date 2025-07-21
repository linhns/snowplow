from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    machine_id: int = 0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
