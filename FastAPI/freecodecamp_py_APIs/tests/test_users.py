import pytest
from jose import jwt

from app import schemas
from app.config import settings
    

def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Welcome to my api!!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())   # here pydantic is already validating the schema and it will throw and error if it's wrong
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    # in order to send this info as a form instead of a noraml json body, we need to put data={}
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})    
    #print(res.json())
    assert res.status_code == 200
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"


@pytest.mark.parametrize("email, password, status_code",[
    ("wrongemail@gmail.com", "password123", 403),
    ("john@gmail.com", "wrongPassword", 403),
    ("wrongemail@gmail.com", "wrongPassword", 403),
    (None, "password123", 422),         # 422 --> schema validation fail
    ("john@gmail.com", None, 422),
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    #assert res.json().get("detail") == "Invalid Credentials"