from django.contrib import admin

from .models import Lemonade

class LemonadeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Lemonade, LemonadeAdmin)