from django import forms

from salesStaff.models import SalesStaff


class RawSalesEntryForm(forms.Form):
    # Staff Name
    # staffs = SalesStaff.objects.all().order_by('name')
    # staff_dropdown_list = []
    # for staff in staffs:
    #     staff_dropdown_list.append((staff.name, staff.name))
    
    # staffName = forms.ChoiceField(
    #     label='Staff Name',
    #     choices=staff_dropdown_list
    # )

    staffName = forms.ModelChoiceField(
        queryset = SalesStaff.objects.all(),
        label='Staff'
    )

# class readOnlySingleFieldForm(forms.Form):

#     currentTotalPrice = forms.CharField(
#         label='Current Total Price',
#         widget=forms.TextInput(attrs={
#             'readonly': 'readonly'
#         })
#     )