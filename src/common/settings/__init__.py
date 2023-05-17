from pydantic import BaseSettings

from src.common.settings.app import ApplicationConfig
from src.common.settings.database import DatabaseConfig
from src.common.settings.util import UtilConfig


class Settings(BaseSettings):
    app: ApplicationConfig = ApplicationConfig()
    db: DatabaseConfig = DatabaseConfig()
    util: UtilConfig = UtilConfig()


settings = Settings()
