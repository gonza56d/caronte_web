# Project
from caronte.periods.models import Period


def create(user, finish_date, budget):
    """Period creation business logic."""

    return Period.objects.create(
        user=user,
        finish_date=finish_date,
        budget=budget
    )
