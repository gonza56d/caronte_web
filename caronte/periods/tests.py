"""Periods tests."""

# Python
from datetime import date, timedelta
import pdb

# Django
from django.test import TestCase

# Mocks
from model_bakery import baker

# Project
from . import services
from caronte.users import services as user_services


class PeriodsTest(TestCase):
    """Class to inherit functionalities to test case classes.
    Provide tools to test periods stuff.
    """

    class DummyPeriod:
        """Dumy period for tests purposes.
        """
        user = baker.make('users.User')
        date = date.today()
        finish_date = date.today() + timedelta(days=30)
        budget = float(30000)
        balance = 0
        dailies = []

    def setUp(self) -> None:
        user = user_services.signup(
            username=self.DummyPeriod.user.username,
            email=self.DummyPeriod.user.email,
            password=self.DummyPeriod.user.password,
            first_name='Illidan',
            last_name='Stormrage'
        )
        self.DummyPeriod.user = user


class PeriodTestCase(PeriodsTest):
    """Run periods tests suite.
    """

    def test_create_period(self) -> None:
        period = services.create(
            user=self.DummyPeriod.user,
            finish_date=self.DummyPeriod.finish_date,
            budget=self.DummyPeriod.budget
        )

        self.assertEqual(
            period.user,
            self.DummyPeriod.user,
            'Created period user is not the same than the dummy period user'
        )

        self.assertEqual(
            period.finish_date,
            self.DummyPeriod.finish_date,
            'Created period finish_date is not the same than the dummy period finish_date'
        )

        self.assertEqual(
            period.budget,
            self.DummyPeriod.budget,
            'Created period budget is not the same than the dummy period budget'
        )
