"""Users tests."""

# Django
from django.http import HttpRequest
from django.test import TestCase

# Project
from . import services


class UsersTest(TestCase):
    """Class to inherit functionalities to test case classes.
    Provide tools to test users stuff.
    """

    class DummyUser:
        """Dummy user for tests purposes.
        """
        username = 'illidan'
        email = 'illidan@wc.com'
        password = 'ghij4689'
        first_name = 'Illidan'
        last_name = 'Stormrage'

    def setUp(self) -> None:
        self.request = HttpRequest()
        dummy = self.DummyUser
        self.user = services.signup(
            username=dummy.username,
            email=dummy.email,
            password=dummy.password,
            first_name=dummy.first_name,
            last_name=dummy.last_name
        )


class SignUpTestCase(UsersTest):

    def test_signup_success(self):
        """Ensure that user attribute are set properly.
        """

        profile = self.user.profile

        self.assertFalse(self.user.is_staff, 'User should not be staff')

        self.assertFalse(self.user.is_superuser, 'User should not be superuser')

        self.assertEqual(
            profile.user,
            self.user,
            'Profile user was not the same than the user itself'
        )

        self.assertEqual(
            profile.first_name,
            self.DummyUser.first_name,
            'Profile first_name was not correct'
        )

        self.assertEqual(
            profile.last_name,
            self.DummyUser.last_name,
            'Profile last_name was not correct'
        )
