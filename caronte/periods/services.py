# Project
from caronte.dailies.models import Daily
from caronte.periods.models import Period


def create(user, finish_date, budget):
    """Period creation business logic."""

    return Period.objects.create(
        user=user,
        finish_date=finish_date,
        budget=budget
    )


def refresh(period: Period) -> Period:
    dailies = Daily.objects.filter(period=period)
    # TODO perform period update
