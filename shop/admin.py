from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'img', 'is_available')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, ProductAdmin)

