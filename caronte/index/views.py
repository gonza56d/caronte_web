"""Index views module."""

# Python
import datetime
# Django
from django.shortcuts import render
from django.views import View
# Project
import services
from caronte.details.forms import DetailForm
from caronte.periods.forms import PeriodForm
from caronte.users.forms import SignupForm
from caronte.utils.constants.strings import CARONTE_INDEX_DESCRIPTION


class MainView(View):
    """
    Main view of the application. Display logic conditions are:
        Authenticated user:
            Existent current Period: the current Period, current Daily with its Details, and previous Dailies.
            No current Period: new Period creation template.
        Anonymous user:
            Application info with login an sign up forms.
    """

    period = None
    daily = None

    def get(self, request):
        """
        Handle get request of main index view page.
        If user is authenticated, look for current period, then if a current Period exists, look (or create a new)
        for the current Daily with its Details. If there is no current Period, the page will display a new Period
        form template to create and start a new one.

        @:return render index/main.html with the proper info and template.
        """

        self.period, self.daily = services.handle_index_view(request)

        return render(request, 'index/main.html', {
            'signup_form': SignupForm(),
            'period_form': PeriodForm(),
            'detail_form': DetailForm(),
            'CARONTE_INDEX_DESCRIPTION': CARONTE_INDEX_DESCRIPTION,
            'period': self.period,
            'daily': self.daily,
            'today': datetime.date.today(),
        })
