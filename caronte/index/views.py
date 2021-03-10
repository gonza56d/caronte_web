"""Index views module."""

# Python
import datetime
# Django
from django.shortcuts import render
from django.views import View
# Project
from caronte.details.forms import DetailForm
from caronte.periods.forms import PeriodForm
from caronte.periods.models import Period
from caronte.users.forms import SignupForm
from caronte.utils.constants.strings import CARONTE_INDEX_DESCRIPTION


class MainView(View):

    period = None

    def get(self, request):
        if request.user.is_authenticated:
            self.period = Period.objects.current(user=request.user)
        return render(request, 'index/main.html', {
            'signup_form': SignupForm(),
            'period_form': PeriodForm(),
            'detail_form': DetailForm(),
            'CARONTE_INDEX_DESCRIPTION': CARONTE_INDEX_DESCRIPTION,
            'period': self.period,
            'today': datetime.date.today(),
        })
