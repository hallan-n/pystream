from domain.models.base import Id
from pydantic import BaseModel, Field, field_validator


class PlanCreate(BaseModel):
    name: str
    max_profiles: int = 1

    @field_validator("name", mode="before")
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

    @field_validator("max_profiles", mode="before")
    def check_max_profiles(cls, value):
        try:
            if value < 1:
                raise Exception(f"O campo Max Profiles deve ser maior que 0.")
            return int(value)
        except:
            raise Exception(f"O campo Max Profiles deve ser um valor numérico.")


class PlanLogin(PlanCreate):
    login_id: int

    @field_validator("login_id", mode="before")
    def check_id(cls, value):
        try:
            return int(value)
        except:
            raise Exception(f"O campo Login id deve ser um valor numérico.")


class Plan(PlanLogin, Id):
    pass
