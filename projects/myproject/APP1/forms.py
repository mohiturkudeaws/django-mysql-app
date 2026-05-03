from django import forms
from . models import Customer
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DataForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
            'InsuranceDuration':DatePickerInput()
        }