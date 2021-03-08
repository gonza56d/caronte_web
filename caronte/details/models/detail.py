"""Details models module."""

# Django
from django.db import models
# Project
from caronte.utils.models import BaseModel


class Detail(BaseModel):

    daily = models.ForeignKey('dailies.Daily', on_delete=models.CASCADE)

    time = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=1000, blank=True, null=True)

    expense = models.DecimalField(max_digits=9, decimal_places=2)
