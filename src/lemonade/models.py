from django.db import models

# Create your models here.
class Lemonade(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)