"""Users signup views."""

# Python
import pdb
# Django
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views import View
# Project
from caronte.users import services
from caronte.users.forms import SignupForm
from caronte.utils.genericfunctions import form_errors_into_string


class SignupView(View):
    """Class that receives users' signup request."""

    form_class = SignupForm

    def post(self, request, *args, **kwargs):
        pdb.set_trace()
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = services.signup(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )
            if user is not None:
                messages.success(request, _('You have registered your account'))
            else:
                messages.error(request, _('Something went wrong, please try again'))
        else:
            errors = form_errors_into_string(form.errors)
            messages.warning(request, errors)
        return redirect('index:main')
