from django.contrib import admin

from .models import Lemonade

# CR: The admin could be more functional...
# Read more on how to customize the admin:
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

class LemonadeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Lemonade, LemonadeAdmin)