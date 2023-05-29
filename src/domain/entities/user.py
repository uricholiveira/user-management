from pydantic import BaseModel, EmailStr, Field

from src.domain.entities.validators.datetime import CustomDatetime
from src.domain.entities.validators.password import PASSWORD_REGEX


class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., regex=PASSWORD_REGEX)


class CreateUserResponse(CreateUserRequest):
    id: str

    class Config:
        orm_mode = True
        json_encoders = {
            CustomDatetime: CustomDatetime.to_str
        }
        fields = {
            'password': {
                'exclude': ...,
            }
        }
