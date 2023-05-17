from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.common.containers import Container
from src.domain.models.health_check import HealthCheckResponse
from src.services.health_check import HealthCheckService

router = APIRouter(prefix="/health_check", tags=["Health Check"])


@router.get("/", response_model=HealthCheckResponse)
@inject
async def health_check(
    health_check_service: HealthCheckService = Depends(
        Provide[Container.health_check_service]
    ),
):
    result = await health_check_service.get_info()
    return result
