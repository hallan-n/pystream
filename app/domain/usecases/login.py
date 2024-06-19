from domain.models.login import Login, LoginSignIn, LoginSignUp


class LoginUseCase:
    def sign_in(self, login: LoginSignIn):
        ...

    def sign_up(self, login: LoginSignUp):
        ...

    def sign_out(self):
        ...

    def get_login(self):
        ...
