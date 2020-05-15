from django.db import models

# Create your models here.
class DrinkOrder(models.Model):

    saleEntry_id = models.IntegerField(default=9999, editable=False)
    lemonade_name = models.CharField(max_length=40)
    quantity = models.IntegerField()