from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


class Base(DeclarativeBase):
    pass


def create_db_engine() -> Engine:
    return create_engine(
        settings.database_url,
        pool_pre_ping=True,
    )


engine = create_db_engine()


def check_database_connection() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False