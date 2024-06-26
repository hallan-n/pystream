import re

from domain.models.base import CreatedAt, Id
from pydantic import BaseModel, EmailStr, Field


class LoginSignInUp(BaseModel):
    email: EmailStr
    password: str = Field(min_length=3, max_length=255)


class Login(LoginSignInUp, CreatedAt, Id):
    pass
