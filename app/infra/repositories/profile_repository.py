from domain.models.profile import Profile, ProfileLogin, ProfileLoginUpdate
from infra.connection import Connection
from infra.schemas import profile_table as schema
from sqlalchemy import and_, delete, insert, select, text, update


class ProfileRepository:
    def __init__(self):
        self.conn = Connection()

    async def create_profile(self, profile: ProfileLogin):
        async with self.conn as conn:
            try:
                stmt = insert(schema).values(**profile.model_dump())
                await conn.execute(stmt)
                return {"success": True, "message": "Created profile."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def exceeds_max_profiles(self, login_id: int):
        async with self.conn as conn:
            try:
                # Juntar as duas querys
                query = text(
                    f"SELECT count(id), max_profiles FROM plan WHERE login_id = {login_id};"
                )
                stmt = await conn.execute(query)

                max_profiles = stmt.fetchone()[0]
                query = text(
                    f"SELECT count(id) FROM profile WHERE login_id = {login_id};"
                )
                stmt = await conn.execute(query)
                profiles = stmt.fetchone()[0]
                exceeds = profiles >= max_profiles
                if exceeds:
                    return {
                        "success": exceeds,
                        "message": f"Your plan does not allow you to create more than {max_profiles} profiles.",
                    }
                return {
                    "success": exceeds,
                    "message": f"Your plan allows you to create {max_profiles} profiles.",
                }
            except Exception as e:
                return {"message": "Error when executing the action."}

    async def update_profile(self, profile: ProfileLoginUpdate):
        async with self.conn as conn:
            try:
                stmt = (
                    update(schema)
                    .where(
                        and_(schema.c.id == profile.id),
                        schema.c.login_id == profile.login_id,
                    )
                    .values(**profile.model_dump())
                )
                result = await conn.execute(stmt)
                if result.rowcount > 0:
                    return {"success": True, "message": "Updated profile."}
                else:
                    return {"success": False, "message": "Profile not found."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def get_all_profiles(self, login_id: int):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(schema.c.login_id == login_id)
                result = await conn.execute(stmt)
                profiles_raw = result.mappings().fetchall()
                profiles = [Profile(**profile) for profile in profiles_raw]
                if profiles:
                    return {"success": True, "data": profiles}
                else:
                    return {"success": False, "message": "Profile not found."}
            except Exception as e:
                return {"success": False, "message": str(e)}

    async def get_profile(self, login_id: int, profile_id: int):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(
                    and_(schema.c.login_id == login_id, schema.c.id == profile_id)
                )
                result = await conn.execute(stmt)
                result = result.mappings().fetchone()
                if result:
                    return {"success": True, "data": Profile(**result)}
                else:
                    return {"success": False, "message": "Profile not found."}
            except Exception as e:
                return {"success": False, "message": str(e)}

    async def delete_profile(self, login_id: int, profile_id: int):
        async with self.conn as conn:
            try:
                stmt = delete(schema).where(
                    and_(schema.c.login_id == login_id, schema.c.id == profile_id)
                )
                result = await conn.execute(stmt)
                if result.rowcount > 0:
                    return {"success": True, "message": "Deleted profile."}
                else:
                    return {"success": False, "message": "Profile not found."}
            except Exception as e:
                await conn.rollback()
                return {"success": False, "message": str(e)}

    async def can_create_profile(self, login_id: int):
        async with self.conn as conn:
            try:
                query = text(f"SELECT 1 FROM plan WHERE login_id = {login_id};")
                stmt = await conn.execute(query)
                can = bool(stmt.fetchone())
                if not can:
                    return {"success": False, "message": "Login does not .have a plan."}
                return {"success": True, "message": "You can create profile."}
            except Exception as e:
                return {"message": "Error when executing the action."}
