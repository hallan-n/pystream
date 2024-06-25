from domain.models.profile import (Profile, ProfileCreate, ProfileLogin,
                                   ProfileLoginUpdate, ProfileUpdate)
from fastapi import HTTPException


class ProfileFactory:
    @staticmethod
    def get_profile(type: str, data: dict):
        try:
            if type == "create":
                return ProfileCreate(**data)
            elif type == "login":
                return ProfileLogin(**data)
            elif type == "update":
                return ProfileUpdate(**data)
            elif type == "login_update":
                return ProfileLoginUpdate(**data)
            elif type == "profile":
                return Profile(**data)
            else:
                raise ValueError(f"Unknown profile type: {type}")
        except Exception as e:
            ...
            # Tratar a exceção da criação do profiles
