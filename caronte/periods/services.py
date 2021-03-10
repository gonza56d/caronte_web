# Project
from caronte.periods.models import Period


def create(user, date_to, budget):
    """Period creation business logic."""

    return Period.objects.create(
        user=user,
        date_to=date_to,
        budget=budget
    )
