from datetime import datetime

from pydantic import BaseModel, Field


class Id(BaseModel):
    id: int = Field(gt=0)


class CreatedAt(BaseModel):
    created_at: datetime = None


class UpdatedAt(BaseModel):
    update_at: datetime = None


class Base(Id, CreatedAt, UpdatedAt):
    pass
