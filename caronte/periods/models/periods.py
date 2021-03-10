"""Periods models module."""

# Python
from datetime import datetime
# Django
from django.db import models
# Project
from caronte.utils.models import BaseModel


class PeriodManager(models.Manager):

    def current(self, user, **kwargs):
        now = datetime.now()
        return self.filter(user=user, created__lte=now, date_to__gt=now, **kwargs)


class Period(BaseModel):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    date_to = models.DateField()

    budget = models.DecimalField(max_digits=9, decimal_places=2)

    objects = PeriodManager()
