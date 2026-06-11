from jhansi_fleet.database import Base, SessionLocal, engine


def test_database_setup() -> None:
    assert Base.metadata is not None
    assert SessionLocal.kw["bind"] is engine
