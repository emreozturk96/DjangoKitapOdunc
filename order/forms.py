from django import forms
from django.forms import DateInput

from functools import partial


# DateInput = partial(forms.DateInput, {'class': 'datepicker'})
class DateInput(forms.DateInput):
    input_type = 'date'


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
