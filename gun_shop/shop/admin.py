from django.contrib import admin
from .models import Products, Cart


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'vanish']
    list_filter = ['vanish']
    list_editable = ['price', 'vanish']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cart)
