from pydantic import BaseModel, Field, field_validator

from app.domain.models.base import Id


class PlanCreate(BaseModel):
    name: str
    max_profiles: int

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
    def check_id(cls, value):
        try:
            return int(value)
        except:
            raise Exception(f"O campo Max Profiles deve ser um valor numérico.")


class Plan(PlanCreate, Id):
    ...
