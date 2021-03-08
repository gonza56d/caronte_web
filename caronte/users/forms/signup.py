# Django
from django import forms
from django.utils.translation import gettext_lazy as _
# Project
from caronte.utils.forms import IconCharField, IconEmailField, IconPasswordField


class SignupForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'] = IconCharField(
            placeholder=_('Username'),
            icon='fas fa-user-circle'
        )

        self.fields['email'] = IconEmailField(
            placeholder=_('Email'),
            icon='fas fa-at'
        )

        self.fields['first_name'] = IconCharField(
            placeholder=_('First name'),
            icon='fas fa-user-edit'
        )

        self.fields['last_name'] = IconCharField(
            placeholder=_('Last name'),
            icon='fas fa-user-edit'
        )

        self.fields['password'] = IconPasswordField(
            placeholder=_('Password'),
            icon='fas fa-key'
        )

        self.fields['re_password'] = IconPasswordField(
            placeholder=_('Password'),
            icon='fas fa-key'
        )
