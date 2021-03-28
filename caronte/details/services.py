"""Details business logic module."""

# Django
from django.db.models import DecimalField
from django.db import transaction

# Project
from caronte.dailies.models import Daily
from caronte.details.models import Detail
from caronte.periods.models import Period
from caronte.users.models import User
from caronte.periods import services as periods_services


def create(user: User, title: str, expense: DecimalField) -> Detail:
    """Handle detail creation logic."""

    with transaction.atomic():
        period = Period.objects.current(user=user)
        period, daily = Daily.objects.from_today(period=period)

        detail = Detail.objects.create(
            daily=daily,
            title=title,
            expense=expense
        )

        daily.expense = float(daily.expense) + float(expense)
        daily.save()

        periods_services.refresh(period=period)
    return detail
