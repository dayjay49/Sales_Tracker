from django.contrib import admin

from .models import DrinkOrder

class DrinkOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'saleEntry_id', 'lemonade_name')

admin.site.register(DrinkOrder, DrinkOrderAdmin)