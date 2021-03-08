# Project
from .forms import LoginForm


class LoginFormMiddleware:
	"""Set LoginForm available in any request if user is not authenticated."""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_authenticated:
			request.login_form = LoginForm(prefix='login')
		return self.get_response(request)
