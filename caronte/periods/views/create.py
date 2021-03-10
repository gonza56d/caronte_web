# Django
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views import View
# Project
from caronte.periods import services
from caronte.periods.forms import PeriodForm
from caronte.utils.genericfunctions import form_errors_into_string


class CreatePeriodView(View):

    form_class = PeriodForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(user=request.user, data=request.POST)
        if form.is_valid():
            period = services.create(
                user=request.user,
                date_to=form.cleaned_data.get('date_to'),
                budget=form.cleaned_data.get('budget')
            )
            if period:
                messages.success(request, _('Period started successfully'))
            else:
                messages.error(request, _('Unknown error occurred, please try again'))
        else:
            errors = form_errors_into_string(form.errors)
            messages.warning(request, errors)
        return redirect('index:main')
