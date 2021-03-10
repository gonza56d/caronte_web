"""Project generic utility functions."""

from django.forms.utils import ErrorDict


def form_errors_into_string(form_erros: ErrorDict) -> str:
    """Receive an ErrorDict and return a CSV-string with each error."""
    errors = ''
    for error in form_erros:
        if errors:
            errors = errors + ', '
        errors = errors + form_erros[error][0].lower()
    return errors
