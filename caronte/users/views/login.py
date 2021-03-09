# Django
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views import View
# Project
from caronte.users import services
from caronte.users.forms import LoginForm


class LoginView(View):

    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, prefix='login')
        if form.is_valid():
            user = services.login(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                messages.success(request, _('You have logged in'))
            else:
                messages.warning(request, _('Wrong username/password'))
        return redirect('index:main')
