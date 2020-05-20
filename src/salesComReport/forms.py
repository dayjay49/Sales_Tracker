from django import forms

from salesStaff.models import SalesStaff

class RawSalesReportForm(forms.Form):
    error_css_class = "error"

    # Staff Name
    staffName = forms.ModelChoiceField(
        queryset = SalesStaff.objects.all(),
        label='Staff',
        empty_label=None
    )

    # Start Date
    startDate = forms.DateTimeField(
        error_messages={'Invalid': "Please enter in provided format -> MM/DD/YYYY H:M AM/PM"},
        label='Start Date and Time',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={
            'placeholder': 'MM/DD/YYYY H:M AM/PM',
            'required': 'required'
        })
    ) 
    
    # End Date
    endDate = forms.DateTimeField(
        error_messages={'Invalid': "Please enter in provided format -> MM/DD/YYYY H:M AM/PM"},
        label='End Date and Time',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={
            'placeholder': 'MM/DD/YYYY H:M AM/PM',
            'required': 'required'
        })
    )