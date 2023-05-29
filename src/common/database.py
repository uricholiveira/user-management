import uuid
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

import arrow
from sqlalchemy import Column, DateTime, String, create_engine, orm
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Session, declared_attr

from src.common.settings import DatabaseConfig


class Database:
    def __init__(self, db_config: DatabaseConfig) -> None:
        self._engine = create_engine(db_config.url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autoflush=db_config.params.auto_flush,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


@as_declarative()
class Base:
    id = Column(
        String,
        primary_key=True,
        default=str(uuid.uuid4()),
        nullable=False,
    )

    created_at = Column(DateTime, default=arrow.utcnow().datetime, nullable=False)
    updated_at = Column(DateTime, onupdate=arrow.utcnow().datetime, nullable=True)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.replace("Model", "").lower()
