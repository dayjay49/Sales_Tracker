from django import forms

class RawSalesReportForm(forms.Form):
    staffName = forms.CharField(
        label='Staff Name', 
        widget=forms.TextInput(attrs={"placeholder": "Full Name"})
    )
    startDate = forms.DateTimeField(
        label='Start Date',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY H:M AM/PM', 'required': 'required'})
        # widget = forms.SelectDateWidget()
        # widget = forms.DateTimeInput(
        #     attrs={
        #         'type': 'datetime-local',
        #         'class': 'form-control'
        #     },
        #     format='%m %d, %Y, %I:%M %p'
        # )
    ) 
    
    endDate = forms.DateTimeField(
        label='End Date',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY H:M AM/PM', 'required': 'required'})
        # widget = forms.SelectDateWidget()
        # widget = forms.DateTimeInput(
        #     attrs={
        #         'type': 'datetime-local',
        #         'class': 'form-control'
        #     },
        #     format='%m %d, %Y, %H:%M'
        # )
        # widget=forms.DateInput(attrs={'placeholder': 'Month Day, Year, Hour:Minute', 'required': 'required'})

    )