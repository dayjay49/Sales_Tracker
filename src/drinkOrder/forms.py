from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet

from .models import DrinkOrder
from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

# # Lemonade Name
# lemonades = Lemonade.objects.all().order_by('name')
# drink_dropdown_list = []
# for drink in lemonades:
#     drink_dropdown_list.append((drink.name, drink.name))

# num_lemonade_types = Lemonade.objects.count()

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
            'quantity': forms.NumberInput(attrs={'min': 1}),
            # 'price_per_drink': forms.HiddenInput()
        }

# class DrinkOrderInlineForm(forms.Form):
#     drink_name = forms.ModelChoiceField(
#         queryset = Lemonade.objects.all(),
#         label='Drink Name'
#     )
#     quantity = forms.IntegerField()
#     drink_price = forms.DecimalField(widget=forms.HiddenInput())

# DrinkOrderFormset = inlineformset_factory(
#     SalesEntry, 
#     DrinkOrder, 
#     fields=('lemonade_name', 'quantity'),
#     extra=1,
#     widgets={
#         'lemonade_name': forms.Select(
#             choices=drink_dropdown_list,
#             attrs={'onchange': "updateTotalPrice(this.value, );"}
#         ),
#         'quantity': forms.NumberInput(attrs={'min': 1, 'default': 0})
#     },
#     can_delete=False,
#     min_num=1,
#     validate_min=True
#     # formset=CustomInlineFormset
# )

DrinkOrderFormset = inlineformset_factory(
    SalesEntry,
    DrinkOrder,
    # fields=('lemonade_name', 'quantity', 'price_per_drink'),
    fields=('lemonade_name', 'quantity'),
    form=DrinkOrderInlineForm,
    can_delete=False,
    extra=1,
    min_num=1,
    validate_min=True,
    max_num=4,
    validate_max=True
)