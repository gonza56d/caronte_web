# Python
from datetime import datetime
# Django
from django.utils import timezone
# Project
from .forms import LoginForm
from .models import User


class LoginFormMiddleware:
	"""Set LoginForm available in any request if user is not authenticated."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_authenticated:
			request.login_form = LoginForm(prefix='login')
		return self.get_response(request)


class SetUpThemeMiddleware:
	"""
	Set up theme for current request.
	"""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		theme = User.Theme.AUTO
		if request.user.is_authenticated:
			theme = request.user.theme

		if theme == User.Theme.AUTO:
			# When theme is set to AUTO, set to LIGHT between 7am and 7pm, and DARK between 7pm and 7am.
			now = timezone.now()
			if now.replace(hour=19) > now >= now.replace(hour=7):
				theme = User.Theme.LIGHT
			else:
				theme = User.Theme.DARK

		request.theme = theme
		return self.get_response(request)
