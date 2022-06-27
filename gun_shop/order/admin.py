from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['fname', 'sname', 'mail', 'citi']
    list_filter = ['citi']
    prepopulated_fields = {'fname': ('sname',)}
