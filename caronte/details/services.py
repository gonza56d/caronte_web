"""Details business logic module."""

# Django
from django.db.models import DecimalField

# Project
from caronte.dailies.models import Daily
from caronte.details.models import Detail


def create(daily: Daily, title: str, expense: DecimalField) -> Detail:
    """Handle detail creation logic."""

    detail = Detail.objects.create(
        daily=daily,
        title=title,
        expense=expense
    )
    return detail
