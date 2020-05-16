from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

# Lemonade Name
lemonades = Lemonade.objects.all().order_by('name')
drink_dropdown_list = []
for drink in lemonades:
    drink_dropdown_list.append((drink.name, drink.name))

# class CustomInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#         for form in self.forms:
#             error_css_class = 'error'
#             if form.cleaned_data['quantity'] <= 0:
#                 # print("FORM VALIDATION FAILED FOR QUANTITY")
#                 form.add_error('quantity', forms.ValidationError("Quantity must be at least 1"))

DrinkOrderFormset = inlineformset_factory(
    SalesEntry, 
    DrinkOrder, 
    fields=('lemonade_name', 'quantity'),
    extra=2,
    widgets={
        'lemonade_name': forms.Select(choices=drink_dropdown_list),
        # 'quantity': forms.NumberInput(attrs={'class':'form-number'})
        'quantity': forms.TextInput(attrs={'min': 1, 'type':'number'})
    },
    can_delete=False,
    # formset=CustomInlineFormset
)
