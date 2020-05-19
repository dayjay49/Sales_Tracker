from django.db import models
from django import forms

from salesEntry.models import SalesEntry
from lemonade.models import Lemonade

# Create your models here.
class DrinkOrder(models.Model):

    saleEntry = models.ForeignKey(
        SalesEntry, 
        on_delete=models.CASCADE,
        related_name='saleEntry'
    )
    # THIS IS ACTUALLY THE LEMONADE MODEL OBJECT ITSELF (not its String name)
    lemonade_name = models.ForeignKey(
        Lemonade, 
        on_delete=models.CASCADE,
        related_name='lemonade_name',
        default=Lemonade.objects.first().name
    )
    # lemonade_name = forms.ModelChoiceField(
    #     queryset = Lemonade.objects.all(),
    #     label='Drink Name'
    # )
    quantity = models.IntegerField(default=0)
    # lemonade_name_id = models.IntegerField(blank=True, default=0)

    price_per_drink = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=Lemonade.objects.first().price,
        # disabled=True
        # widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    order_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=Lemonade.objects.first().price,
    )

    def __str__(self):
        return "Drink Order with ID = " + str(self.id)