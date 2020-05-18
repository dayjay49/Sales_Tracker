from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

# class CustomInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#         for form in self.forms:
#             error_css_class = 'error'
#             if form.cleaned_data['quantity'] <= 0:
#                 # print("FORM VALIDATION FAILED FOR QUANTITY")
#                 form.add_error('quantity', forms.ValidationError("Quantity must be at least 1"))

class DrinkOrderInlineForm(forms.ModelForm):
    class Meta:
        model = DrinkOrder
        # fields = ['lemonade_name', 'quantity', 'price_per_drink']
        fields = ['lemonade_name', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'min': 1, 
                'default': 0,
                # 'onchange': "alert(this.value);"
            }),
            'lemonade_name': forms.Select(attrs={
                # 'onchange': "alert(this.options[this.selectedIndex].text);"
            }),
            # 'price_per_drink': forms.HiddenInput()
        }

DrinkOrderFormset = inlineformset_factory(
    SalesEntry,
    DrinkOrder,
    # fields=('lemonade_name', 'quantity', 'price_per_drink'),
    fields=('lemonade_name', 'quantity'),
    form=DrinkOrderInlineForm,
    can_delete=False,
    extra=0,
    min_num=1,
    validate_min=True,
    max_num=Lemonade.objects.count(),
    validate_max=True
)