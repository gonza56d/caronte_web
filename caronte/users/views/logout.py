# Django
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views import View
# Project
from caronte.users import services


class LogoutView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            services.logout(request)
            messages.success(request, _('You have logged out'))
        return redirect('index:main')
