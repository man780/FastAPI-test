"""
Conftest file
"""
import pytest

from starlette.testclient import TestClient
from faker import Faker

from main import app

fake = Faker()


@pytest.fixture(scope="module")
def test_app():
    """
    Fixture for test app
    :return:
    """
    client = TestClient(app)
    yield client


@pytest.fixture
def random_user_data():
    """
    Fixture for generate random user data
    :return: dict
    """
    username = fake.user_name()
    email = fake.email()
    full_name = fake.name()
    return {"username": username, "email": email, "full_name": full_name}
