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
    
    quantity = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return "Drink Order with ID = " + str(self.id)