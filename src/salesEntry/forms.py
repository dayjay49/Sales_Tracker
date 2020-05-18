from django import forms

from salesStaff.models import SalesStaff


class RawSalesEntryForm(forms.Form):

    staffName = forms.ModelChoiceField(
        queryset = SalesStaff.objects.all(),
        label='Staff',
        empty_label=None
    )

# class readOnlySingleFieldForm(forms.Form):

#     currentTotalPrice = forms.CharField(
#         label='Current Total Price',
#         widget=forms.TextInput(attrs={
#             'readonly': 'readonly'
#         })
#     )