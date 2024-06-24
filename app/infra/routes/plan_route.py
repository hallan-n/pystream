from domain.models.plan import PlanCreate, PlanLogin
from domain.usecases.plan_usecase import PlanUseCase
from fastapi import APIRouter, Depends
from infra.security import Security


class PlanRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tags=["Plan"], prefix="/plan")
        self.usecase = PlanUseCase()
        self._setup()

    def _setup(self):
        self.add_api_route("/add", self.add_plan, methods=["POST"])
        self.add_api_route("/att", self.update_plan, methods=["POST"])
        self.add_api_route("/get", self.get_plan, methods=["GET"])
        self.add_api_route("/del", self.remove_plan, methods=["DELETE"])

    async def add_plan(
        self, plan: PlanCreate, token: dict = Depends(Security.decode_token)
    ):
        """Cria um plano."""
        return await self.usecase.add_plan(
            PlanLogin(**plan.model_dump(), login_id=token["id"])
        )

    async def update_plan(
        self, plan: PlanCreate, token: dict = Depends(Security.decode_token)
    ):
        """Atualiza um plano."""
        return await self.usecase.update_plan(
            PlanLogin(**plan.model_dump(), login_id=token["id"])
        )

    async def get_plan(self, token: dict = Depends(Security.decode_token)):
        """Pega as informações do plano."""
        return await self.usecase.get_plan(token["id"])

    async def remove_plan(self, token: dict = Depends(Security.decode_token)):
        """Remove um plano."""
        return await self.usecase.remove_plan(login_id=token["id"])

    async def get_plan(self, token: dict = Depends(Security.decode_token)):
        """Pega as informações do plano."""
        return await self.usecase.get_plan(token["id"])


plan = PlanRouter()
