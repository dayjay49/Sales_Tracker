from django import forms
from django.forms import inlineformset_factory

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

# Lemonade Name
lemonades = Lemonade.objects.all().order_by('name')
drink_dropdown_list = []
for drink in lemonades:
    drink_dropdown_list.append((drink.name, drink.name))

DrinkOrderFormset = inlineformset_factory(
    SalesEntry, 
    DrinkOrder, 
    fields=('lemonade_name', 'quantity'),
    extra=2,
    widgets={
        'lemonade_name': forms.Select(choices=drink_dropdown_list),
        'quantity': forms.NumberInput(attrs={'class':'form-number'})
    },
    can_delete=False
)
