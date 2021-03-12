"""Dailies models module."""

# Django
from django.db import models
# Project
from caronte.utils.models import BaseModel


class Daily(BaseModel):

    period = models.ForeignKey('periods.Period', on_delete=models.CASCADE)

    notes = models.CharField(max_length=1000, blank=True, null=True)

    date = models.DateField(auto_now_add=True)

    expense = models.DecimalField(max_digits=9, decimal_places=2)

    remainder = models.DecimalField(max_digits=9, decimal_places=2)

    @property
    def today_expense(self):
        from caronte.details.models import Detail
        details = Detail.objects.filter(daily=self)
        __expense = 0
        for detail in details:
            __expense += detail.expense
        return __expense

    @property
    def today_remainder(self):
        return self.period.daily_budget - self.today_expense
