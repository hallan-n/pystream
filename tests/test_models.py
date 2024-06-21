import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/")))


from datetime import datetime

from app.domain.models.login import Login, LoginSignInUp
from app.domain.models.plan import Plan, PlanCreate
from app.domain.models.profile import Profile, ProfileCreate


def test_login():
    assert Login(
        id=1, email="teste@teste.com", password="senha_teste", created_at=datetime.now()
    )
    assert LoginSignInUp(email="teste@teste.com", password="senha_teste")


def test_profile():
    assert Profile(id=1, name="teste", icon="teste", login_id=1)
    assert ProfileCreate(icon="teste", name="teste")


def test_plan():
    assert Plan(id=1, max_profiles=3, name="teste")
    assert PlanCreate(max_profiles=3, name="teste")
