"""Detail creation tests."""

# Python
from datetime import timedelta, datetime
# Project
from caronte.details import services as detail_services
from caronte.periods import services as period_services
from caronte.utils.tests import BaseTest, TestUtils


class DetailTest(BaseTest, TestUtils):

    def setUp(self) -> None:
        self.user = self.get_user()
        period_services.create(
            user=self.user,
            finish_date=datetime.today() + timedelta(days=20),
            budget=20000
        )

    def test_create_detail(self):
        detail = detail_services.create(
            user=self.user,
            title='Test detail',
            expense=35.5
        )
        self.assertIsNotNone(detail, 'Details: Detail is None after calling services.create() function')
