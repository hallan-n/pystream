from domain.models.base import Id
from pydantic import BaseModel, Field, field_validator


class PlanCreate(BaseModel):
    name: str = Field(min_length=3, max_length=255)
    max_profiles: int = Field(ge=0)


class PlanLogin(PlanCreate):
    login_id: int = Field(ge=0)


class Plan(PlanLogin, Id):
    pass
