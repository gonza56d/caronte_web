"""Details models module."""

# Django
from django.db import models
from django.utils import timezone
# Project
from caronte.dailies.models import Daily
from caronte.periods.models import Period
from caronte.utils.models import BaseModel


class DetailManager(models.Manager):

    def from_today(self, period: Period, **kwargs):
        today = timezone.now()
        try:
            daily = Daily.objects.get_or_create(period=period, date=today, defaults={
                'period': period,
                'expense': 0,
                'remainder': period.daily_budget
            })
            return self.filter(daily=daily[0])
        except Daily.DoesNotExist:
            return self.none()


class Detail(BaseModel):

    daily = models.ForeignKey('dailies.Daily', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)

    expense = models.DecimalField(max_digits=9, decimal_places=2)

    objects = DetailManager()
