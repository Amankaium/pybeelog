from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone', 'notes', 'data')
    ordering = ['data']

admin.site.register(Order, OrderAdmin)