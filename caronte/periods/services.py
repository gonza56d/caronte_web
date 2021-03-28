# Python
from datetime import date, timedelta
# Django
from django.utils.translation import gettext as _
from django.utils import timezone
# Project
from caronte.periods.models import Period
from caronte.utils.genericfunctions import days_until_today


def create(user, finish_date, budget):
    """Period creation business logic."""

    return Period.objects.create(
        user=user,
        finish_date=finish_date,
        budget=budget
    )


def get_dailies_creating_missings(period: Period):
    """
    Fetch all the dailies from Period and create Dailies which are missing until today. This prevents missing dailies
    when User doesn't connect to the app for one or more days.
    """
    from caronte.dailies.models import Daily

    dailies = Daily.objects.filter(period=period)

    dailies_quantity = dailies.count()
    expected_dailies_quantity = days_until_today(start_date=period.date)
    missing_dailies = expected_dailies_quantity - dailies_quantity

    i = 0  # 0 to n count to multiply created daily balance
    for n in reversed(range(missing_dailies)):
        i += 1
        daily_date = dailies.last().date - timedelta(days=n+1)
        Daily.objects.create(
            period=period,
            notes=_('Inactive day'),
            date=daily_date,
            expense=0,
            remainder=period.daily_budget,
            balance=period.balance + period.daily_budget * i
        )
    if missing_dailies > 0:
        dailies = Daily.objects.filter(period=period)
    return dailies


def refresh(period: Period) -> Period:
    """
    Get all the Dailies from the Period and calculate the current balance, then update the Period.
    :param period: Period to update the balance.
    :return: Period with updated balance.
    """
    dailies = get_dailies_creating_missings(period)
    balance = 0
    for daily in dailies:
        balance += period.daily_budget - daily.expense
    period.balance = balance
    period.save()
    return period
