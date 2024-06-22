from fastapi import status
from fastapi.responses import JSONResponse
from infra.repositories.plan_repository import PlanRepository

from app.domain.models.plan import Plan, PlanCreate


class PlanUseCase:
    def __init__(self) -> None:
        self.repository = PlanRepository()

    async def create_plan(self, plan: PlanCreate):
        resp = await self.repository.create_plan(plan)
        return JSONResponse(content=resp, status_code=status.HTTP_201_CREATED)

    async def update_plan(self, plan: Plan):
        resp = await self.repository.update_plan(plan)
        json_resp = JSONResponse(content=resp, status_code=status.HTTP_200_OK)
        if not resp["sucess"]:
            json_resp.status_code = status.HTTP_400_BAD_REQUEST
        return json_resp

    async def get_plan(self, id: int):
        resp = await self.repository.get_plan(id)
        if not resp["sucess"]:
            JSONResponse(content=resp, status_code=status.HTTP_404_NOT_FOUND)
        return resp["data"]
