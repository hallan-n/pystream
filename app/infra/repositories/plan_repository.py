from domain.models.login import Login, LoginSignInUp
from domain.models.plan import Plan, PlanLogin
from infra.connection import Connection
from infra.schemas import plan_table as schema
from sqlalchemy import insert, select, update


class PlanRepository:
    def __init__(self):
        self.conn = Connection()

    async def add_plan(self, plan: PlanLogin):
        async with self.conn as conn:
            try:
                stmt = insert(schema).values(**plan.model_dump())
                await conn.execute(stmt)
                return {"success": True, "message": "Created Plan."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": "Error creating a Plan."}

    async def update_plan(self, plan: Plan):
        async with self.conn as conn:
            try:
                stmt = (
                    update(schema)
                    .where(schema.c.id == plan.id)
                    .values(**plan.model_dump())
                )
                result = await conn.execute(stmt)
                if result.rowcount > 0:
                    return {"success": True, "message": "Updated Plan."}
                else:
                    return {"success": False, "message": f"Plan not found."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def get_plan(self, id: int):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(schema.c.login_id == id)
                result = await conn.execute(stmt)
                plan = result.mappings().fetchone()
                if plan:
                    return {"success": True, "data": Plan(**plan)}
                else:
                    return {"success": False, "message": "Plan not found."}
            except Exception as e:
                return {"success": False, "message": str(e)}
