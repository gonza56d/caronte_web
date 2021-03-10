"""Post models admin."""

# Django
from django.contrib import admin
# Project
from caronte.periods.models import Period


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    """Period model admin."""

    pass
