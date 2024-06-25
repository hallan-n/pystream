import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/")))


from datetime import datetime

from app.domain.models.login import Login, LoginSignInUp
from app.domain.models.plan import Plan, PlanCreate, PlanLogin
from app.domain.models.profile import Profile, ProfileCreate, ProfileUpdate, ProfileLogin, ProfileLoginUpdate


def test_models():
    assert Login(
        id=1, email="teste@teste.com", password="senha_teste", created_at=datetime.now()
    )
    assert LoginSignInUp(email="teste@teste.com", password="senha_teste")

    assert ProfileCreate(icon="teste", name="teste")
    assert ProfileUpdate(id=1, icon="teste", name="teste")
    assert Profile(id=1, name="teste", icon="teste", login_id=1)
    assert ProfileLogin(name="teste", icon="teste",  login_id=1)
    assert ProfileLoginUpdate(id=1, name="teste", icon="teste", login_id=1)

    assert Plan(id=1, max_profiles=3, name="teste", login_id=1)
    assert PlanLogin(max_profiles=3, name="teste", login_id=1)
    assert PlanCreate(max_profiles=3, name="teste")
