from datetime import datetime

from pydantic import BaseModel, field_validator


class Id(BaseModel):
    id: int

    @field_validator("id", mode="before")
    def check_id(cls, value):
        try:
            return int(value)
        except:
            raise Exception(f"O campo ID deve ser um valor numérico.")


class CreatedAt(BaseModel):
    created_at: datetime = None


class UpdatedAt(BaseModel):
    updated_at: datetime = None


class Base(Id, CreatedAt, UpdatedAt):
    ...
