"""Periods models module."""

# Django
from django.db import models
# Project
from caronte.utils.models import BaseModel


class Period(BaseModel):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    date_from = models.DateField(auto_now_add=True)

    date_to = models.DateField()
