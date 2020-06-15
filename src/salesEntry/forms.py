from django import forms
from django.forms import inlineformset_factory

from salesStaff.models import SalesStaff
from .models import SalesEntry, DrinkOrder

class RawSalesEntryForm(forms.Form):

    staffName = forms.ModelChoiceField(
        queryset = SalesStaff.objects.all(),
        label='Staff',
        empty_label=None
    )

class DrinkOrderInlineForm(forms.ModelForm):
    class Meta:
        model = DrinkOrder
        fields = [
            'lemonade', 
            'quantity'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'min': 1, 
                'default': 0,
                'onchange': "updateQuantity(this.value, this.id);",
                'required': 'required'
            }),
            'lemonade': forms.Select(attrs={
                'onchange': "updateDrink(this.options[this.selectedIndex].text, this.id);"
            })
        }
DrinkOrderFormset = inlineformset_factory(
    SalesEntry,
    DrinkOrder,
    fields=('lemonade', 'quantity'),
    form=DrinkOrderInlineForm,
    can_delete=False,
    extra=0,
    min_num=1,
    validate_min=True,
    max_num=4,
    validate_max=True
)

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
