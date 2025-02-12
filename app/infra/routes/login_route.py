from domain.models.login import LoginSignInUp, LoginUpdate
from domain.usecases.login_usecase import LoginUseCase
from fastapi import APIRouter, Depends
from infra.security import Security


class LoginRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tags=["Login"], prefix="/login")
        self.usecase = LoginUseCase()
        self._setup()

    def _setup(self):
        self.add_api_route("/in/", self.sign_in, methods=["POST"])
        self.add_api_route("/up/", self.sign_up, methods=["POST"])
        self.add_api_route("/att/", self.update_login, methods=["PUT"])
        self.add_api_route("/out/", self.sign_out, methods=["POST"])
        self.add_api_route("/get/", self.get_login, methods=["GET"])

    async def sign_in(self, login: LoginSignInUp):
        """Pegar o acesso da API."""
        return await self.usecase.sign_in(login)

    async def sign_up(self, login: LoginSignInUp):
        """Cria um login."""
        return await self.usecase.sign_up(login)

    async def update_login(
        self, login: LoginSignInUp, token: dict = Depends(Security.decode_token)
    ):
        """Cria um login."""
        resp = await self.usecase.update_login(
            LoginUpdate(**login.model_dump(), id=token["id"])
        )
        await self.usecase.sign_out(str(token))
        return resp

    async def sign_out(self, token: dict = Depends(Security.decode_token)):
        """Revoga o acesso na API."""
        return await self.usecase.sign_out(str(token))

    async def get_login(self, token: dict = Depends(Security.decode_token)):
        """Pega os dados o usuário atual."""
        return await self.usecase.get_login(token["id"])


login = LoginRouter()
