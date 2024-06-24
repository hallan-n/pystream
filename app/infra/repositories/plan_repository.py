from domain.models.plan import Plan, PlanLogin
from infra.connection import Connection
from infra.schemas import plan_table as schema
from sqlalchemy import delete, insert, select, text, update


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

    async def remove_plan(self, login_id: int):
        async with self.conn as conn:
            try:
                stmt = delete(schema).where(schema.c.login_id == login_id)
                result = await conn.execute(stmt)
                if result.rowcount > 0:
                    return {"success": True, "message": "Deleted Plan."}
                else:
                    return {"success": False, "message": "Plan not found."}
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

    async def has_plan(self, login_id: int):
        async with self.conn as conn:
            try:
                query = text(f"SELECT 1 FROM plan WHERE login_id = {login_id};")
                stmt = await conn.execute(query)
                has = bool(stmt.fetchone())
                if not has:
                    return {"success": has, "message": "Login does not have a plan."}
                return {"success": has, "message": "Login already has a plan."}
            except Exception as e:
                return {"message": "Error when executing the action."}
