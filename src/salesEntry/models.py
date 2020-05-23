from django.db import models

from lemonade.models import Lemonade

# SalesEntry Model
class SalesEntry(models.Model):

    staffName = models.CharField(max_length=40)
    staffID = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

# DrinkOrder Model
class DrinkOrder(models.Model):

    saleEntry = models.ForeignKey(
        SalesEntry, 
        on_delete=models.CASCADE,
        related_name='saleEntry'
    )
    # THIS IS ACTUALLY THE LEMONADE MODEL OBJECT ITSELF (not its String name)
    lemonade = models.ForeignKey(
        Lemonade, 
        on_delete=models.CASCADE,
        related_name='lemonade',
        # default=Lemonade.objects.first().name
    )
    
    quantity = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return "Drink Order with ID = " + str(self.id)