from django import forms
from .models import Booking
from django.forms.widgets import DateInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-sm',
                'placeholder': 'Select start date'
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-sm',
                'placeholder': 'Select return date'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date must be before end date.")
