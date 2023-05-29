from pydantic import BaseModel, EmailStr, Field

from src.domain.entities.validators.datetime import CustomDatetime
from src.domain.entities.validators.password import PASSWORD_REGEX


class LoginRequest(BaseModel):
    username: EmailStr
    password: str = Field(..., regex=PASSWORD_REGEX)
