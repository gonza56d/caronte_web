# Django
from django.http import HttpRequest
# Project
from caronte.dailies.models import Daily
from caronte.periods.models import Period


def handle_index_view(request: HttpRequest) -> (Period, Daily):
    period = None
    daily = None
    if request.user.is_authenticated:
        period = Period.objects.current(user=request.user)
        period, daily = Daily.objects.from_today(period=period)
    return period, daily
