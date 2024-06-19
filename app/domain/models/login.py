import re

from pydantic import BaseModel, Field, field_validator

from app.domain.models.base import CreatedAt, Id


class LoginSignIn(BaseModel):

    email: str
    password: str

    @field_validator("email", "password", mode="before")
    def check_len(cls, value, field: Field):
        if len(value) > 255:
            raise Exception(
                f"O campo {field.field_name.capitalize()} não deve exceder 255 caracteres."
            )
        if len(value) < 3:
            raise Exception(
                f"O campo {field.field_name.capitalize()} não deve ser menor que 3 caracteres."
            )
        return value

    @field_validator("email", mode="before")
    def check_email(cls, value):
        if not re.match(r".+@.+\.[A-Za-z]{2,6}", value):
            raise Exception(f"Email inválido.")
        return value


class LoginSignUp(CreatedAt): ...


class Login(LoginSignUp, Id): ...
