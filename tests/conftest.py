import pytest

from starlette.testclient import TestClient
from faker import Faker

from main import app

fake = Faker()


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture
def random_user_data():
    username = fake.user_name()
    email = fake.email()
    full_name = fake.name()
    return {"username": username, "email": email, "full_name": full_name}
