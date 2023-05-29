from contextlib import AbstractContextManager
from typing import Callable, Type

from sqlalchemy.orm import Session

from src.domain.entities.user import CreateUserRequest
from src.domain.models.user import UserModel


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> list[Type[UserModel]]:
        with self.session_factory() as session:
            return session.query(UserModel).all()

    async def get_by_id(self, user_id: str) -> Type[UserModel] | None:
        with self.session_factory() as session:
            return session.query(UserModel).filter_by(id=user_id).first()

    async def get_by_email(self, email: str) -> Type[UserModel] | None:
        with self.session_factory() as session:
            return session.query(UserModel).filter_by(email=email).first()

    async def create(self, data: CreateUserRequest) -> UserModel:
        user = UserModel(**data.dict())
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)

        return user
