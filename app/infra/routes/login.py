from domain.models.login import Login, LoginSignIn, LoginSignUp
from fastapi import APIRouter, HTTPException


class LoginRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tags=["Login"], prefix="/login")
        self._setup()

    def _setup(self):
        self.add_api_route("/in/", self.sign_in, methods=["POST"])
        self.add_api_route("/up/", self.sign_up, methods=["POST"])
        self.add_api_route("/out/", self.sign_out, methods=["POST"])
        self.add_api_route("/get/", self.get_login, methods=["GET"])

    async def sign_in(self, login: LoginSignIn):
        ...

    async def sign_up(self, login: LoginSignUp):
        ...

    async def sign_out(self):
        ...

    async def get_login(self):
        ...


login = LoginRouter()
