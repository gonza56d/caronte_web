"""Periods forms."""

# Python
from datetime import datetime
# Django
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# Project
from caronte.periods.models import Period
from caronte.utils.forms import IconDecimalField, IconDateField


class PeriodForm(forms.ModelForm):

    class Meta:
        model = Period
        fields = ['finish_date', 'budget']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['finish_date'] = IconDateField(icon='fas fa-calendar-alt', placeholder=_('Finish date'))
        self.fields['budget'] = IconDecimalField(icon='fas fa-dollar-sign', placeholder=_('Budget'))

    def clean(self):
        cleaned_data = super()
        now = datetime.now()
        split_date = cleaned_data.get('finish_date').split('-')
        existing_period = Period.objects.current(user=self.user)
        if existing_period:
            raise ValidationError(_('You already have an active Period'))
        errors = ''
        if datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])) <= now:
            errors += _('Period finish date must be after today')
        if float(get('budget')) < 30:
            if errors:
                errors += ', '
            errors += _('Budget cannot be less than $30')
        if errors:
            raise ValidationError(errors)
