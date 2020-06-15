from django.contrib import admin

from .models import SalesStaff

class SalesStaffAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(SalesStaff, SalesStaffAdmin)