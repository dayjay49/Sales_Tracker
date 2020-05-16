from django.db import models

from salesEntry.models import SalesEntry

# Create your models here.
class DrinkOrder(models.Model):

    saleEntry = models.ForeignKey(SalesEntry, on_delete=models.CASCADE)
    lemonade_name = models.CharField(max_length=40)
    quantity = models.IntegerField()