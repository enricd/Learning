from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models

#from alembic import command     # optionally to create and drop db and tables instead of using sqlalchemy

# --- the fixtures in this files are automatically imported to any other test file by Pytest ---

# Creating a db only for testing
# Adapt env variables for test
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# simple way to create all necessary tables in the fastapi_test db, otherwise we could use alembic
# Base.metadata.create_all(bind=engine)


# def override_get_db(): 
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    # --- run before we run the test ---
    #command.upgrade("head")    # optionally instead of using sqlalchemy Base
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    def override_get_db():
        try:
            yield session
        finally:
            session.close() 

    app.dependency_overrides[get_db] = override_get_db      # now we can have access not only to the client but also to the db to make queries at every test function if we pass the session as well
    yield TestClient(app)   
    # --- run after the test finishes ---
    # Base.metadata.drop_all(bind=engine)
    #command.downgrade("base")  # optionally, alembic needs to be properly set then


# this fixture will allow to create a user to later test to login with it, making test_login_user() independent of test_create_user()
@pytest.fixture
def test_user(client):
    user_data = {"email": "john@gmail.com",
                "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]

    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {"email": "john2@gmail.com",
                "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]

    return new_user


@pytest.fixture
def token(test_user):

    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [
        {
            "title": "1st title",
            "content": "1st content",
            "owner_id": test_user["id"],
        },
        {
            "title": "2nd title",
            "content": "2nd content",
            "owner_id": test_user["id"],
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id": test_user["id"],
        },
        {
            "title": "extra title",
            "content": "extra content",
            "owner_id": test_user2["id"],
        },
        ]

    session.add_all([models.Post(**post) for post in posts_data])
    session.commit()
    session.query(models.Post).all()

    posts = session.query(models.Post).all()
    return  posts