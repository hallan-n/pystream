from domain.models.plan import Plan, PlanCreate, PlanLogin
from fastapi import status
from fastapi.responses import JSONResponse
from infra.repositories.plan_repository import PlanRepository


class PlanUseCase:
    def __init__(self) -> None:
        self.repository = PlanRepository()

    async def add_plan(self, plan: PlanLogin):
        resp = await self.repository.add_plan(plan)
        json_resp = JSONResponse(content=resp, status_code=status.HTTP_201_CREATED)
        if not resp["success"]:
            json_resp.status_code = status.HTTP_400_BAD_REQUEST
        return json_resp

    async def update_plan(self, plan: PlanLogin):
        current_plan = await self.repository.get_plan(plan.login_id)
        resp = await self.repository.update_plan(
            Plan(**plan.model_dump(), id=current_plan["data"].id)
        )
        json_resp = JSONResponse(content=resp, status_code=status.HTTP_200_OK)
        if not resp["success"]:
            json_resp.status_code = status.HTTP_400_BAD_REQUEST
        return json_resp

    async def get_plan(self, user_id: int):
        resp = await self.repository.get_plan(user_id)
        if not resp["success"]:
            JSONResponse(content=resp, status_code=status.HTTP_404_NOT_FOUND)
        return resp["data"]
