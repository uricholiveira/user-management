from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from src.common.containers import Container
from src.domain.entities.auth import LoginRequest
from src.domain.entities.user import CreateUserResponse, CreateUserRequest
from src.services.auth import AuthService
from src.services.user import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
@inject
async def login(
        data: LoginRequest,
        auth_service: AuthService = Depends(
            Provide[Container.auth_service]
        ),
):
    result = await auth_service.login(data=data)
    return result
