from typing import Type

from fastapi import HTTPException
from passlib.context import CryptContext

from src.domain.entities.user import CreateUserRequest
from src.domain.models.user import UserModel
from src.repositories.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def get_user_by_id(self, user_id: str) -> Type[UserModel] | None:
        return await self._repository.get_by_id(user_id=user_id)

    async def get_user_by_email(self, email: str) -> Type[UserModel] | None:
        return await self._repository.get_by_email(email=email)

    async def create_user(self, data: CreateUserRequest) -> UserModel:
        has_user = await self.get_user_by_email(data.email)
        if has_user:
            raise HTTPException(status_code=409, detail={"message": "User cannot be created"})

        data.password = self.get_password_hash(data.password)
        return await self._repository.create(data=data)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)
