from pydantic import BaseSettings


class ApplicationConfig(BaseSettings):
    title: str = "Backend"
    version: str = "0.1.0"
    description: str = "A simple backend api template"
    host: str = "localhost"
    port: int = 3000
    access_token_expire_minutes: int = 15
