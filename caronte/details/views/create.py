"""Create Detail views."""

# Python
# Django
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView
# Project
from caronte.dailies.models import Daily
from caronte.details.models import Detail
from caronte.periods.models import Period


class CreateDetailView(CreateView):

    model = Detail
    fields = ['title', 'expense']

    def get(self, request, *args, **kwargs):
        return redirect('index:main')

    def post(self, request, *args, **kwargs):
        period = Period.objects.current(user=request.user)
        today = timezone.now()
        request.POST['daily'] = Daily.objects.get(period=period, created=today)
        return super().post(request, *args, **kwargs)
