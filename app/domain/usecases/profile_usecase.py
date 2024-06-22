from infra.repositories.login_repository import LoginRepository


class ProfileUseCase:
    def __init__(self) -> None:
        self.repository = LoginRepository()

    async def create_profile(self):
        ...
