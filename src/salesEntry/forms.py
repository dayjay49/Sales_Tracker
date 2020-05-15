from django import forms

from .models import SalesEntry

# class SalesEntryForm(forms.ModelForm):
#     class Meta:
#         model = SalesEntry
#         fields = [
#             'staffName',
#         ]

class RawSalesEntryForm(forms.Form):
    staffName = forms.CharField(label='Staff Name', widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
    drinkName = forms.CharField(label='Lemonade Name', widget=forms.TextInput(attrs={"placeholder": "Drink Name"}))
    quantity = forms.IntegerField(label='Quantity')