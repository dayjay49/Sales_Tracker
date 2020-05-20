from django import forms

from salesStaff.models import SalesStaff
# from .models import SalesReport

# class: SalesReportForm(forms.ModelForm):
#     class Meta:
#         model = SalesReport
#         fields = [
#             'staff',
#             'startDate',
#             'endDate'
#         ]
#         widgets = {
#             'startDate': forms.DateInput(attrs={
#                 'placeholder': 'MM/DD/YYYY H:M AM/PM'
#             })
#         }

class RawSalesReportForm(forms.Form):
    error_css_class = "error"

    # # Staff Name
    # staffs = SalesStaff.objects.all().order_by('name')
    # staff_dropdown_list = []
    # for staff in staffs:
    #     staff_dropdown_list.append((staff.name, staff.name))
    
    # staffName = forms.ChoiceField(
    #     label='Staff Name',
    #     choices=staff_dropdown_list
    # )

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