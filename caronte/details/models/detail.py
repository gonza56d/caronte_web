"""Details models module."""

# Django
from django.db import models
from django.utils import timezone
# Project
from caronte.utils.models import BaseModel


class Detail(BaseModel):

    daily = models.ForeignKey('dailies.Daily', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)

    expense = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta(BaseModel.Meta):
        ordering = ['created']
