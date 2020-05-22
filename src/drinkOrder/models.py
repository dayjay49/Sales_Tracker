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
    # CR: right - and it should be named accordingly - lemonade (not lemonade_name)
    lemonade_name = models.ForeignKey(
        Lemonade, 
        on_delete=models.CASCADE,
        related_name='lemonade_name',
        # default=Lemonade.objects.first().name
    )
    
    quantity = models.IntegerField(
        default=0,
    )
    # CR: I see that you decided to implement commission calculation in the report.
    # What happens if the employee was promoted? Should his commission recalculated retroactively?

    def __str__(self):
        return "Drink Order with ID = " + str(self.id)