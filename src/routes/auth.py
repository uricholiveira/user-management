from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.common.containers import Container
from src.domain.entities.auth import LoginRequest
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
@inject
async def login(
    data: LoginRequest,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    result = await auth_service.login(data=data)
    return result
