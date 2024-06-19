from datetime import datetime

from app.domain.models.login import Login, LoginSignIn, LoginSignUp
from app.domain.models.profile import Profile, ProfileCreate


def test_login():
    assert Login(
        id=1, email="teste@teste.com", password="senha_teste", created_at=datetime.now()
    )
    assert LoginSignUp(email="teste@teste.com", password="senha_teste")
    assert LoginSignIn(email="teste@teste.com", password="senha_teste")


def test_profile():
    assert Profile(id=1, name="teste", icon="teste", login_id=1)
    assert ProfileCreate(icon="teste", name="teste")