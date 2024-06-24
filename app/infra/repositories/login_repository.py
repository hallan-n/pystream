from domain.models.login import Login, LoginSignInUp
from infra.connection import Connection
from infra.schemas import login_table as schema
from sqlalchemy import insert, select, update


class LoginRepository:
    def __init__(self):
        self.conn = Connection()

    async def create_account(self, login: LoginSignInUp):
        async with self.conn as conn:
            try:
                stmt = insert(schema).values(**login.model_dump())
                await conn.execute(stmt)
                return {"success": True, "message": "Created account."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def update_account(self, login: Login):
        async with self.conn as conn:
            try:
                stmt = (
                    update(schema)
                    .where(schema.c.id == login.id)
                    .values(**login.model_dump())
                )
                result = await conn.execute(stmt)
                if result.rowcount > 0:
                    return {"success": True, "message": "Updated account."}
                else:
                    return {"success": False, "message": f"Account not found."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def get_account_by_id(self, id: int):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(schema.c.id == id)
                result = await conn.execute(stmt)
                account = result.mappings().fetchone()
                if account:
                    return {"success": True, "data": Login(**account)}
                else:
                    return {"success": False, "message": "Account not found."}
            except Exception as e:
                return {"success": False, "message": str(e)}

    async def get_account_by_login(self, login: LoginSignInUp):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(schema.c.email == login.email)
                result = await conn.execute(stmt)
                account = result.mappings().fetchone()
                if account:
                    return {"success": True, "data": Login(**account)}
                else:
                    return {"success": False, "message": "Account not found."}
            except Exception as e:
                return {"success": False, "message": str(e)}
