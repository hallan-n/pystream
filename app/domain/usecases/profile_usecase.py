from domain.models.profile import ProfileLogin, ProfileLoginUpdate
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from infra.repositories.profile_repository import ProfileRepository


class ProfileUseCase:
    def __init__(self) -> None:
        self.repository = ProfileRepository()

    async def create_profile(self, profile: ProfileLogin):
        exceeds = await self.repository.exceeds_max_profiles(profile.login_id)
        if exceeds["success"]:
            raise HTTPException(
                detail=exceeds["message"], status_code=status.HTTP_403_FORBIDDEN
            )
        resp = await self.repository.create_profile(profile)
        return JSONResponse(content=resp, status_code=status.HTTP_201_CREATED)

    async def get_all_profiles(self, login_id: int):
        profiles = await self.repository.get_all_profiles(login_id)
        if not profiles["success"]:
            raise HTTPException(
                detail=profiles["message"], status_code=status.HTTP_404_NOT_FOUND
            )
        return profiles["data"]

    async def get_profile(self, login_id: int, profile_id: int):
        profiles = await self.repository.get_profile(login_id, profile_id)
        if not profiles["success"]:
            raise HTTPException(
                detail=profiles["message"], status_code=status.HTTP_404_NOT_FOUND
            )
        return profiles["data"]

    async def delete_profile(self, login_id: int, profile_id: int):
        profile = await self.repository.delete_profile(login_id, profile_id)
        if not profile["success"]:
            raise HTTPException(
                detail=profile["message"], status_code=status.HTTP_400_BAD_REQUEST
            )
        return JSONResponse(content=profile, status_code=status.HTTP_200_OK)

    async def update_profile(self, profile: ProfileLoginUpdate):
        resp = await self.repository.update_profile(profile)
        if not resp["success"]:
            raise HTTPException(
                detail=resp["message"], status_code=status.HTTP_400_BAD_REQUEST
            )
        return JSONResponse(content=resp, status_code=status.HTTP_200_OK)
