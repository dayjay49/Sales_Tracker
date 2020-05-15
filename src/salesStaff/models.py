from django.db import models

# Create your models here.
class SalesStaff(models.Model):
    name=models.CharField(max_length=30)
    position=models.CharField(max_length=15)
    commissionRate=models.DecimalField(max_digits=10, decimal_places=2)

