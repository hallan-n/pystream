from domain.models.plan import Plan, PlanLogin
from fastapi import status
from fastapi.responses import JSONResponse
from infra.repositories.plan_repository import PlanRepository


class PlanUseCase:
    def __init__(self) -> None:
        self.repository = PlanRepository()

    async def remove_plan(self, login_id: int):
        has_plan = await self._has_plan(login_id)
        if not has_plan["success"]:
            return JSONResponse(
                content={"success": False, "message": has_plan["message"]},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        resp = await self.repository.remove_plan(login_id)
        return JSONResponse(content=resp, status_code=status.HTTP_200_OK)

    async def add_plan(self, plan: PlanLogin):
        has_plan = await self._has_plan(plan.login_id)
        if has_plan["success"]:
            return JSONResponse(
                content={"success": False, "message": has_plan["message"]},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        resp = await self.repository.add_plan(plan)
        return JSONResponse(content=resp, status_code=status.HTTP_201_CREATED)

    async def update_plan(self, plan: PlanLogin):
        has_plan = await self._has_plan(plan.login_id)
        if not has_plan["success"]:
            return JSONResponse(
                {"success": False, "message": has_plan["message"]},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        current_plan = await self.repository.get_plan(plan.login_id)

        if not current_plan["success"]:
            return JSONResponse(
                content=current_plan["message"], status_code=status.HTTP_400_BAD_REQUEST
            )

        resp = await self.repository.update_plan(
            Plan(**plan.model_dump(), id=current_plan["data"].id)
        )

        json_resp = JSONResponse(content=resp, status_code=status.HTTP_200_OK)
        return json_resp

    async def get_plan(self, login_id: int):
        resp = await self.repository.get_plan(login_id)
        if not resp["success"]:
            return JSONResponse(content=resp, status_code=status.HTTP_404_NOT_FOUND)
        return resp["data"]

    async def _has_plan(self, login_id: int):
        return await self.repository.has_plan(login_id)
