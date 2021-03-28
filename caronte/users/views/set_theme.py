# Django
from django.shortcuts import redirect
# Project
from caronte.users.models import User


def set_theme_view(request, theme):
    """
    Set user theme_option in session. Also set value to authenticated user's theme attribute and update user.
    :param request: Django's request
    :param theme: Option to set in session (a/l/d) -> (auto/light/dark)
    :return: redirect to the same page where the request came from, or index's main if theme option is corrupt.
    """
    request.session['theme_option'] = User.Theme(theme).name
    if request.user.is_authenticated:
        request.user.theme = User.Theme(theme)
        request.user.save()
    return redirect(request.META.get('HTTP_REFERER', 'index:main'))
