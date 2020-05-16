from django.db import models

# Create your models here.
class SalesEntry(models.Model):

    staffName = models.CharField(max_length=40)
    staffID = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

