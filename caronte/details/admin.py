"""Detail model admin."""

# Django
from django.contrib import admin
# Project
from caronte.details.models import Detail


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    """Detail model admin."""

    pass
