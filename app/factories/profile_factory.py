from domain.models.profile import (Profile, ProfileCreate, ProfileLogin,
                                   ProfileLoginUpdate, ProfileUpdate)
from fastapi import HTTPException, status
from pydantic import ValidationError


class ProfileFactory:
    profile_types = {
        "create": ProfileCreate,
        "login": ProfileLogin,
        "update": ProfileUpdate,
        "login_update": ProfileLoginUpdate,
        "profile": Profile,
    }

    @staticmethod
    def get_profile(type: str, data: dict):
        try:
            profile_class = ProfileFactory.profile_types.get(type)
            if not profile_class:
                raise ValueError(f"Unknown profile type: {type}")
            return profile_class(**data)
        except ValidationError as e:
            error = e.errors()[0]
            raise HTTPException(
                detail=f"{error['loc'][0].title()}: {error['msg']}",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
