from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Jhansi Fleet"
    database_url: str = "sqlite:///./jhansi_fleet.db"

    model_config = SettingsConfigDict(
        env_prefix="JHANSI_FLEET_",
    )


settings = Settings()
