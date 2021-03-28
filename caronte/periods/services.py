# Project
from caronte.periods.models import Period


def create(user, finish_date, budget):
    """Period creation business logic."""

    return Period.objects.create(
        user=user,
        finish_date=finish_date,
        budget=budget
    )


def refresh(period: Period) -> Period:
    """
    Get all the Dailies from the Period and calculate the current balance, then update the Period.
    :param period: Period to update the balance.
    :return: Period with updated balance.
    """
    from caronte.dailies.models import Daily
    dailies = Daily.objects.filter(period=period)
    balance = 0
    for daily in dailies:
        balance += period.daily_budget - daily.expense
    period.balance = balance
    period.save()
    return period
