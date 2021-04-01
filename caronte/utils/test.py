# Python
import pdb
# Django
from django.test import TestCase, Client
from django.shortcuts import reverse
# Project
from caronte.users.models import User
from caronte.utils.genericfunctions import get_or_none


class AuthenticatedTestCase(TestCase):
    """Test case to inherit from which implements signup and login test cases, and provide a user attribute."""

    class DummyUser:
        username = 'testuser'
        email = 'test@user.com'
        password = 'testuser'
        first_name = 'Test'
        last_name = 'User'

    def setUp(self) -> None:
        c = Client()
        response = c.post(reverse('users:signup'), {'username': self.DummyUser.username, 'email': self.DummyUser.email,
                                                    'password': self.DummyUser.password, 'first_name': self.DummyUser.first_name,
                                                    'last_name': self.DummyUser.last_name})
        self.assertEquals(response.status_code, 302, 'Signup: Response status code was not 302 (redirect)')
        self.user = get_or_none(model=User, username=self.DummyUser.username)
        self.assertIsNotNone(self.user, 'User was not found after signup')
        response = c.post(reverse('users:login'), {'username': self.DummyUser.username, 'password': self.DummyUser.password})
        self.assertEquals(response.status_code, 302, 'Login: Response status code was not 302 (redirect)')
        self.assertTrue(self.user.is_authenticated, 'Login: User was not authenticated after login request')
