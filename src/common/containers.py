from pathlib import Path

from dependency_injector import containers, providers

from src.common.database import Database
from src.common.settings import Settings
from src.repositories.health_check import HealthCheckRepository
from src.services.health_check import HealthCheckService


class Container(containers.DeclarativeContainer):
    path = Path().absolute().joinpath("src/routes")
    modules = ["src.routes." + x.stem for x in path.iterdir()]
    wiring_config = containers.WiringConfiguration(modules=modules)

    settings = Settings()

    # Add Singletons (Database, Authentication, etc)
    # Example
    db = providers.Singleton(Database, settings.db)

    # Add provider.Factory for Repositories|Services
    # Example
    health_check_repository = providers.Factory(
        HealthCheckRepository, session_factory=db.provided.session
    )
    health_check_service = providers.Factory(
        HealthCheckService, health_check_repository=health_check_repository
    )
