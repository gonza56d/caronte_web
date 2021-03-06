# Django
from django import forms


class IconCharField(forms.CharField):
    """Django CharField with custom icon attr."""
    
    def __init__(self, *, icon='', placeholder=None, max_length=None,
                 min_length=None, strip=True, empty_value='', **kwargs):
        super().__init__(**kwargs)
        self.icon = icon
        self.widget = forms.TextInput(attrs={'class': 'form-control'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder


class IconEmailField(forms.EmailField):
    """Django EmailField with custom icon attr."""
    
    def __init__(self, icon='', placeholder=None, **kwargs):
        super().__init__(**kwargs)
        self.icon = icon
        self.widget = forms.EmailInput(attrs={'class': 'form-control'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder


class IconPasswordField(forms.CharField):
    """Django CharField with custom icon attr and password widget."""
    
    def __init__(self, *, icon='', placeholder=None, max_length=None, 
                 min_length=None, strip=True, empty_value='', **kwargs):
        super().__init__(**kwargs)
        self.icon = icon
        self.widget = forms.PasswordInput(attrs={'class': 'form-control'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder


class IconDateField(forms.CharField):
    """Django CharField with custom icon attr for dates."""

    def __init__(self, *, icon='', placeholder=None, max_length=None,
                 min_length=None, strip=True, empty_value='', **kwargs):
        super().__init__(**kwargs)
        self.icon = icon
        self.widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder


class IconDecimalField(forms.CharField):
    """Django NumberField with custom icon attr and two decimals."""

    def __init__(self, *, icon='', placeholder=None, max_length=None,
                 min_length=None, strip=True, empty_value='', **kwargs):
        super().__init__(**kwargs)
        self.icon = icon
        self.widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder
