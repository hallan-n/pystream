import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/")))

from pytest import fixture
from datetime import datetime
from app.domain.models.login import LoginSignInUp



@fixture
def sign_in():
    return LoginSignInUp(email='teste@teste.com', password='teste123')

@fixture
def sign_up():
    return LoginSignInUp(email='teste@tes1t1e.com', password='teste123')
    
    