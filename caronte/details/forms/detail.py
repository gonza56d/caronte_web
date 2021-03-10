
# Django
from django import forms
from django.utils.translation import gettext_lazy as _
# Project
from caronte.details.models import Detail
from caronte.utils.forms import IconCharField, IconDecimalField


class DetailForm(forms.ModelForm):

    class Meta:
        model = Detail
        fields = ['title', 'expense']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = IconCharField(icon='fas fa-pen', placeholder=_('Description'))
        self.fields['expense'] = IconDecimalField(icon='fas fa-dollar-sign', placeholder=_('Expense'))
