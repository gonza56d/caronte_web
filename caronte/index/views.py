"""Index views module."""

# Django
from django.shortcuts import render
from django.views import View
# Project
from caronte.periods.forms import PeriodForm
from caronte.periods.models import Period
from caronte.users.forms import SignupForm
from caronte.utils.constants.strings import CARONTE_INDEX_DESCRIPTION


class MainView(View):

    signup_form = SignupForm()
    period_form = PeriodForm()
    period = None

    def get(self, request):
        if request.user.is_authenticated:
            self.period = Period.objects.current(user=request.user)
        return render(request, 'index/main.html', {
            'signup_form': self.signup_form,
            'period_form': self.period_form,
            'CARONTE_INDEX_DESCRIPTION': CARONTE_INDEX_DESCRIPTION,
            'period': self.period,
        })
