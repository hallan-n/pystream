from domain.models.base import CreatedAt, Id, UpdatedAt
from pydantic import BaseModel, EmailStr, Field


class LoginSignInUp(BaseModel):
    email: EmailStr
    password: str = Field(min_length=3, max_length=255)


class LoginUpdate(LoginSignInUp, Id):
    pass


class Login(LoginUpdate, CreatedAt, UpdatedAt):
    pass
