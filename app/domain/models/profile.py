from domain.models.base import Base, Id
from pydantic import BaseModel, Field, field_validator


class ProfileCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    icon: str = Field(..., min_length=2, max_length=255)


class ProfileLogin(ProfileCreate):
    login_id: int = Field(..., gt=0)


class ProfileUpdate(ProfileCreate, Id):
    pass


class ProfileLoginUpdate(ProfileLogin, Id):
    pass


class Profile(ProfileLogin, Base):
    pass
