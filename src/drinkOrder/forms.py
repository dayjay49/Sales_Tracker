from django import forms
from django.forms import inlineformset_factory
# from django.forms import BaseInlineFormSet

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

class DrinkOrderInlineForm(forms.ModelForm):
    class Meta:
        model = DrinkOrder
        fields = [
            'lemonade_name', 
            'quantity'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'min': 1, 
                'default': 0,
                'onchange': "updateQuantity(this.value, this.id);",
                'required': 'required'
            }),
            'lemonade_name': forms.Select(attrs={
                'onchange': "updateDrink(this.options[this.selectedIndex].text, this.id);"
            })
        }

DrinkOrderFormset = inlineformset_factory(
    SalesEntry,
    DrinkOrder,
    fields=('lemonade_name', 'quantity'),
    form=DrinkOrderInlineForm,
    can_delete=False,
    extra=0,
    min_num=1,
    validate_min=True,
    max_num=4,
    validate_max=True
)