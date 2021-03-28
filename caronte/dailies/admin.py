"""Daily model admin."""

# Django
from django.contrib import admin
# Project
from caronte.dailies.models import Daily


@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    """Daily model admin."""

    pass
