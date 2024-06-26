from domain.models.base import Id
from domain.models.profile import (ProfileCreate, ProfileLogin,
                                   ProfileLoginUpdate, ProfileUpdate)
from domain.usecases.profile_usecase import ProfileUseCase
from fastapi import APIRouter, Depends
from infra.security import Security


class ProfileRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tags=["Profile"], prefix="/profile")
        self.usecase = ProfileUseCase()
        self._setup()

    def _setup(self):
        self.add_api_route("/add", self.create_profile, methods=["POST"])
        self.add_api_route("/att", self.update_profile, methods=["PUT"])
        self.add_api_route("/get/{id}", self.get_profile, methods=["GET"])
        self.add_api_route("/get", self.get_all_profiles, methods=["GET"])
        self.add_api_route("/del", self.delete_profile, methods=["DELETE"])

    async def create_profile(
        self, profile: ProfileCreate, token: dict = Depends(Security.decode_token)
    ):
        """Cria um Perfil."""

        return await self.usecase.create_profile(
            ProfileLogin(**profile.model_dump(), login_id=token["id"])
        )

    async def get_all_profiles(self, token: dict = Depends(Security.decode_token)):
        """Pega todos os Perfis."""
        return await self.usecase.get_all_profiles(token["id"])

    async def get_profile(
        self, profile_id: int, token: dict = Depends(Security.decode_token)
    ):
        """Pega um Perfil."""
        return await self.usecase.get_profile(token["id"], profile_id)

    async def delete_profile(
        self, profile_id: Id, token: dict = Depends(Security.decode_token)
    ):
        """Deleta um Perfil."""
        return await self.usecase.delete_profile(token["id"], profile_id.id)

    async def update_profile(
        self, profile: ProfileUpdate, token: dict = Depends(Security.decode_token)
    ):
        """Atualiza um Perfil."""
        return await self.usecase.update_profile(
            ProfileLoginUpdate(**profile.model_dump(), login_id=token["id"])
        )


profile = ProfileRouter()
