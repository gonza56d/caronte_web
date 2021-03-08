"""Project string constants."""

from django.utils.translation import gettext_lazy as _


CARONTE_INDEX_DESCRIPTION = _(
    """<strong>Caronte</strong> is an application for expense management.<br>
    You can set a <b>Period</b>, where you determine how much money you have and the date it ends.<br>
    It starts on creation date. Only one <b>Period</b> can be active at a time.<br>
    Once a <b>Period</b> is active, the system will calculate what is the money media that you can spend per day,
    so that you are aware of how much money you're saving or how much you're overspending."""
)
