"""Dailies models module."""

# Django
from django.db import models
from django.utils import timezone
# Project
from caronte.details.models import Detail
from caronte.periods import services as period_services
from caronte.periods.models import Period
from caronte.utils.models import BaseModel


class DailyManager(models.Manager):

    @staticmethod
    def from_today(period: Period):
        """
        Look for current Daily or create a new if it does not exists.
        Refresh current Period status if a new Daily has been created.

        :param period: User's Period to search today's Daily.
        :return: Today's Daily with its current Details list.
        """
        today = timezone.now().date()
        get_or_create = Daily.objects.get_or_create(period=period, date=today, defaults={
            'period': period,
            'expense': 0,
            'remainder': period.daily_budget
        })
        daily, created = get_or_create[0], get_or_create[1]
        daily.details = Detail.objects.filter(daily=daily)
        period.dailies = Daily.objects.filter(period=period)
        if created:
            period = period_services.refresh(period)
        return period, daily


class Daily(BaseModel):

    period = models.ForeignKey('periods.Period', on_delete=models.CASCADE)

    notes = models.CharField(max_length=1000, blank=True, null=True)

    date = models.DateField()

    expense = models.DecimalField(max_digits=9, decimal_places=2)

    remainder = models.DecimalField(max_digits=9, decimal_places=2)

    balance = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=True, default=0)

    objects = DailyManager()

    @property
    def today_remainder(self):
        return self.period.daily_budget - self.expense

    class Meta(BaseModel.Meta):
        ordering = ['date']
