"""Periods models module."""

# Python
from datetime import datetime
# Django
from django.db import models
from django.utils import timezone
# Project
from caronte.utils.models import BaseModel


class PeriodManager(models.Manager):

    def current(self, user, **kwargs):
        now = timezone.now()
        try:
            return self.get(user=user, date__lte=now, finish_date__gte=now, **kwargs)
        except Period.DoesNotExist:
            return None


class Period(BaseModel):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    finish_date = models.DateField()

    budget = models.DecimalField(max_digits=9, decimal_places=2)

    objects = PeriodManager()

    @property
    def daily_budget(self):
        start_date = datetime.strptime(str(self.date), "%Y-%m-%d")
        end_date = datetime.strptime(str(self.finish_date), "%Y-%m-%d")
        days = abs((end_date - start_date).days)
        return self.budget / days
