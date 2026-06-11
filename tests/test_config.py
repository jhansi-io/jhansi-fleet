from jhansi_fleet.config import Settings


def test_settings_defaults() -> None:
    settings = Settings()

    assert settings.app_name == "Jhansi Fleet"
    assert settings.database_url == "sqlite:///./jhansi_fleet.db"
