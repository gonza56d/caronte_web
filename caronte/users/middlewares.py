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
		"""
		Request's "theme_option" is the chosen theme in session, while request's "theme" is the assigned theme by
		the middleware logic. We must store them separately since, for instance, the theme_option could be "AUTO", then
		the middleware logic will set the theme to LIGHT or DARK depending on server time, hence the user would lose the
		"AUTO" option being replaced by LIGHT/DARK if we'd stored them in the same session variable.
		"""

		# Must be called after view was processed, so that theme change can be applied before the middleware
		response = self.get_response(request)

		# First, try to set the chosen theme either from authenticated user's attribute or from anonymous' session variable.
		if request.user.is_authenticated:
			theme = request.user.theme.name
		else:
			try:
				theme = request.session['theme_option']
			except KeyError:  # Set to AUTO by default.
				theme = User.Theme.AUTO.name
				request.session['theme_option'] = User.Theme.AUTO.name

		if not theme or theme == User.Theme.AUTO.name:
			# When theme_option is set to AUTO, set theme to LIGHT between 7am and 7pm, and DARK between 7pm and 7am.
			now = timezone.now()
			if now.replace(hour=19) > now >= now.replace(hour=7):
				theme = User.Theme.LIGHT.name
			else:
				theme = User.Theme.DARK.name

		request.session['theme'] = theme
		return response
