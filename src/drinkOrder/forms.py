from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

class DrinkOrderInlineForm(forms.ModelForm):
    class Meta:
        model = DrinkOrder
        fields = [
            'lemonade_name', 
            'quantity', 
            'price_per_drink',
            'order_price'
        ]
        # fields = ['lemonade_name', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'min': 1, 
                'default': 0,
                'onchange': "updateQuantity(this.value, this.id);",
                'required': 'required'
            }),
            'lemonade_name': forms.Select(attrs={
                'onchange': "updateDrink(this.options[this.selectedIndex].text, this.id);"
            }),
            'price_per_drink': forms.NumberInput(attrs={
                # 'style': "display:none;",
                'onchange': "alert(this);"
            }),
            'order_price': forms.NumberInput(attrs={
                # 'style': "display:none;",
                'onchange': "alert(this);"
            }),
            # 'price_per_drink': forms.HiddenInput(),
            # 'order_price': forms.HiddenInput()
        }

DrinkOrderFormset = inlineformset_factory(
    SalesEntry,
    DrinkOrder,
    fields=('lemonade_name', 'quantity', 'price_per_drink', 'order_price'),
    # fields=('lemonade_name', 'quantity'),
    form=DrinkOrderInlineForm,
    can_delete=False,
    extra=0,
    min_num=1,
    validate_min=True,
    max_num=Lemonade.objects.count(),
    validate_max=True
)