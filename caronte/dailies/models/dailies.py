"""Dailies models module."""

# Django
from django.db import models
from django.utils import timezone
# Project
from caronte.details.models import Detail
from caronte.periods.models import Period
from caronte.utils.models import BaseModel


class DailyManager(models.Manager):

    def from_today(self, period: Period, **kwargs):
        today = timezone.now()
        try:
            daily = Daily.objects.get_or_create(period=period, date=today, defaults={
                'period': period,
                'expense': 0,
                'remainder': period.daily_budget
            })[0]
            daily.details = Detail.objects.filter(daily=daily)
            return daily
        except Daily.DoesNotExist:
            return self.none()


class Daily(BaseModel):

    period = models.ForeignKey('periods.Period', on_delete=models.CASCADE)

    notes = models.CharField(max_length=1000, blank=True, null=True)

    date = models.DateField(auto_now_add=True)

    expense = models.DecimalField(max_digits=9, decimal_places=2)

    remainder = models.DecimalField(max_digits=9, decimal_places=2)

    objects = DailyManager()

    @property
    def today_expense(self):
        __expense = 0
        for detail in self.details:
            __expense += detail.expense
        return __expense

    @property
    def today_remainder(self):
        return self.period.daily_budget - self.today_expense
