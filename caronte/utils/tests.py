# Django
from django.test import TestCase, Client
# Project
from caronte.users import services as user_services
from caronte.users.models import User


class TestUtils:

    class DummyUser:
        username = 'testuser'
        email = 'test@user.com'
        password = 'testuser'
        first_name = 'Test'
        last_name = 'User'

    def get_user(self) -> User:
        return user_services.signup(
            username=self.DummyUser.username,
            email=self.DummyUser.email,
            password=self.DummyUser.password,
            first_name=self.DummyUser.first_name,
            last_name=self.DummyUser.last_name
        )


class BaseTest(TestCase):
    """Test case to inherit from which provides common setup and a DummyUser nested class."""

    def setUp(self) -> None:
        self.c = Client()
