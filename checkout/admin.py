from django.contrib import admin
from .models import Order
from modeltranslation.admin import TranslationAdmin


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone', 'notes', 'data', 'paid')
    ordering = ['data']
