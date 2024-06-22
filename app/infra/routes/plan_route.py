from fastapi import APIRouter, Depends
from infra.security import Security

from app.domain.usecases.plan_usecase import PlanUseCase


class PlanRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tags=["Plan"], prefix="/plan")
        self.usecase = PlanUseCase()
        self._setup()

    def _setup(self):
        self.add_api_route("/", self.create_plan, methods=["POST"])
        self.add_api_route("/", self.update_plan, methods=["POST"])
        self.add_api_route("/", self.get_plan, methods=["GET"])

    async def create_plan(self, token: dict = Depends(Security.decode_token)):
        """Cria um plano."""
        ...

    async def update_plan(self, token: dict = Depends(Security.decode_token)):
        """Atualiza um plano."""
        ...

    async def get_plan(self, token: dict = Depends(Security.decode_token)):
        """Pega as informações do plano."""
        ...


plan = PlanRouter()
