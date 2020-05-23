from django.contrib import admin

from .models import SalesEntry, DrinkOrder
# Register your models here.

# this is so that we can still see the date time of when this entry/sale was made
class SalesEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'id')

admin.site.register(SalesEntry, SalesEntryAdmin)

# class DrinkOrderAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'saleEntry_id', 'lemonade_name')

# admin.site.register(DrinkOrder, DrinkOrderAdmin)