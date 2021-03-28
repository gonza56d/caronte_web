"""Project generic utility functions."""

# Python
from datetime import datetime
# Django
from django.forms.utils import ErrorDict
from django.utils import timezone


def form_errors_into_string(form_erros: ErrorDict) -> str:
    """Receive an ErrorDict and return a CSV-string with each error."""
    errors = ''
    for error in form_erros:
        if errors:
            errors = errors + ', '
        errors = errors + form_erros[error][0].lower()
    return errors


def days_until_today(start_date: datetime) -> int:
    """Get how many days are between start_date and today"""

    now = timezone.now().date()
    return abs((now - start_date).days)
