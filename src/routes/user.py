from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.common.containers import Container
from src.common.util.jwt import JwtUtils
from src.domain.entities.user import CreateUserResponse, CreateUserRequest
from src.services.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/profile", response_model=CreateUserResponse, dependencies=[Depends(JwtUtils.jwt_authentication)])
@inject
async def profile(
        user_info: dict = Depends(JwtUtils.jwt_authentication),
        user_service: UserService = Depends(
            Provide[Container.user_service]
        ),
):
    result = await user_service.get_user_by_email(email=user_info.get("sub"))
    return result


@router.get("/{user_id:str}", response_model=CreateUserResponse)
@inject
async def get_user(
        user_id: str,
        user_service: UserService = Depends(
            Provide[Container.user_service]
        ),
):
    result = await user_service.get_user_by_id(user_id=user_id)
    return result


@router.post("/", response_model=CreateUserResponse)
@inject
async def create_user(
        data: CreateUserRequest,
        user_service: UserService = Depends(
            Provide[Container.user_service]
        ),
):
    result = await user_service.create_user(data=data)
    return result
