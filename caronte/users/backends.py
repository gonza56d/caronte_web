"""Authentication backends."""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


UserModel = get_user_model()


class UserBackend(ModelBackend):
    """
    Class for authentication logic.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Implement authentication by finding user by either username or email.
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        username = username.lower()
        try:
            user = UserModel._default_manager.get(
                Q(username=username) | Q(email=username)
            )
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
