from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class LogForm(forms.Form):
    name = forms.CharField(max_length=200)
    date = forms.DateField(widget=DateInput())
    hours_worked = forms.DecimalField(
        max_digits=4,
            validators=[
                MaxValueValidator(10),
                MinValueValidator(0.5)
            ]
    )