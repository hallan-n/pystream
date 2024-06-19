from domain.models.base import CreatedAt, Id
from pydantic import Field, field_validator


class ProfileCreate(CreatedAt):
    name: str
    icon: str

    @field_validator("name", "icon", mode="before")
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


class Profile(ProfileCreate, Id):
    login_id: int

    @field_validator("login_id", mode="before")
    def check_id(cls, value):
        try:
            return int(value)
        except:
            raise Exception(f"O campo Login ID deve ser um valor numérico.")
