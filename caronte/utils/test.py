# Django
from django.test import TestCase, Client
from django.shortcuts import reverse
# Project
from caronte.users.models import User


class AuthenticatedTestCase(TestCase):
    """Test case to inherit from which implements signup and login test cases, and provide a user attribute."""

    def setUp(self) -> None:
        c = Client()
        c.post(reverse('users:signup'), {'username': 'testuser', 'email': 'test@user.com', 'password': 'testuser',
                                         'first_name': 'Test', 'last_name': 'User'})
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testuser',
                                             first_name='Test', last_name='User')
        c.post(reverse('users:login'))
