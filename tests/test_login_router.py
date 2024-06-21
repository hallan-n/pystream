import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/")))

from app.main import app
from fastapi.testclient import TestClient
import json
from pytest import mark

client = TestClient(app)

def test_sign_in(sign_in):
    response = client.post('http://localhost:8000/login/in/', content=json.dumps(sign_in.model_dump()))
    assert response.status_code == 200

@mark.skip
def test_sign_up(sign_up):
    response = client.post('http://localhost:8000/login/up/', content=json.dumps(sign_up.model_dump()))
    assert response.status_code == 201

@mark.skip
def test_sign_out(sign_in_up):
    response = client.get('/out/')
    assert response.status_code == 201

@mark.skip
def test_get_login(sign_in_up):
    response = client.get('/get/')
    assert response.status_code == 201
