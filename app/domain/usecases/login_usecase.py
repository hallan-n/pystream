from domain.models.login import Login, LoginSignInUp, LoginUpdate
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from infra.repositories.login_repository import LoginRepository
from infra.security import Security


class LoginUseCase:
    def __init__(self) -> None:
        self.repository = LoginRepository()

    async def sign_up(self, login: LoginSignInUp):
        login.password = Security.hashed(login.password)
        resp = await self.repository.create_account(login)
        return JSONResponse(content=resp, status_code=status.HTTP_201_CREATED)

    async def update_login(self, login: LoginUpdate):
        login.password = Security.hashed(login.password)
        resp = await self.repository.update_account(login)
        return JSONResponse(content=resp, status_code=status.HTTP_200_OK)

    async def sign_in(self, login: LoginSignInUp):
        resp = await self.repository.get_account_by_login(login)
        if not resp["success"]:
            raise HTTPException(
                detail=resp["message"], status_code=status.HTTP_404_NOT_FOUND
            )
        if not Security.check_hash(resp["data"].password, login.password):
            raise HTTPException(
                detail="Incorrect password.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        data = resp["data"]

        access_token = Security.create_access_token(
            data={"id": data.id, "email": data.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}

    async def get_login(self, id):
        resp = await self.repository.get_account_by_id(id)
        if not resp["success"]:
            raise HTTPException(
                detail=resp["message"], status_code=status.HTTP_404_NOT_FOUND
            )

        data = resp["data"].model_dump()
        return Login(**data)

    async def sign_out(self, token: str):
        try:
            Security.revoke_access_token(token)
            return {"success": True, "message": "Logout completed."}
        except Exception as e:
            return {"success": False, "message": e}
