"""Dailies models module."""

# Django
from django.db import models
# Project
from caronte.utils.models import BaseModel


class Daily(BaseModel):

    period = models.ForeignKey('periods.Period', on_delete=models.CASCADE)

    notes = models.CharField(max_length=1000, blank=True, null=True)

    date = models.DateField(auto_now_add=True)
