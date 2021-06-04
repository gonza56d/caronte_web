"""Periods tests."""

# Python
from datetime import date, timedelta

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

    def setUp(self) -> None:
        self.period = baker.make('periods.Period')


class PeriodTestCase(PeriodsTest):
    """Run periods tests suite.
    """

    def test_create_period(self) -> None:
        period = services.create(
            user=self.period.user,
            finish_date=self.period.finish_date,
            budget=self.period.budget
        )

        self.assertEqual(
            period.user,
            self.period.user,
            'Created period user is not the same than the dummy period user'
        )

        self.assertEqual(
            period.finish_date,
            self.period.finish_date,
            'Created period finish_date is not the same than the dummy period finish_date'
        )

        self.assertEqual(
            period.budget,
            self.period.budget,
            'Created period budget is not the same than the dummy period budget'
        )
