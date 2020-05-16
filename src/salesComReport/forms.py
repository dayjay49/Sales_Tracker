from django import forms

from salesStaff.models import SalesStaff

class RawSalesReportForm(forms.Form):
    # Staff Name
    staffs = SalesStaff.objects.all().order_by('name')
    staff_dropdown_list = []
    for staff in staffs:
        staff_dropdown_list.append((staff.name, staff.name))
    
    staffName = forms.ChoiceField(
        label='Staff Name',
        choices=staff_dropdown_list
    )

    # Start Date
    startDate = forms.DateTimeField(
        label='Start Date and Time',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY H:M AM/PM', 'required': 'required'})
    ) 
    
    # End Date
    endDate = forms.DateTimeField(
        label='End Date and Time',
        input_formats = ['%m/%d/%Y %I:%M %p'],
        widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY H:M AM/PM', 'required': 'required'})
    )