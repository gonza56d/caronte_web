"""Create Detail views."""

# Django
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
# Project
from caronte.dailies.models import Daily
from caronte.details import services
from caronte.details.forms import DetailForm
from caronte.periods.models import Period
from caronte.utils.genericfunctions import form_errors_into_string


class CreateDetailView(View):

    form_model = DetailForm

    def get(self, request, *args, **kwargs):
        return redirect('index:main')

    def post(self, request, *args, **kwargs):
        form = self.form_model(data=request.POST)
        if not form.is_valid():
            errors = form_errors_into_string(form.errors)
            messages.warning(request, errors)
        else:
            period = Period.objects.current(user=request.user)
            today = timezone.now()
            detail = services.create(
                daily=Daily.objects.get(period=period, date=today),
                title=form.cleaned_data.get('title'),
                expense=form.cleaned_data.get('expense')
            )
            if detail:
                messages.success(request, _('Detail added'))
            else:
                messages.error(request, _('Unkown error occurred'))
        return redirect('index:main')
