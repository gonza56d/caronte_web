# Django
from django import forms
from django.utils.translation import gettext_lazy as _
# Project
from caronte.utils.forms import IconCharField, IconPasswordField


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'] = IconCharField(
            placeholder=_('Username'),
            icon='fas fa-user'
        )

        self.fields['password'] = IconPasswordField(
            placeholder=_('Password'), 
            icon='fas fa-key'
        )
