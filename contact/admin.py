from django.contrib import admin

# Register your models here.
from .models import Feedback, Subscribe


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone', 'email','title',"created_at")
    list_display_links = ('id', 'title')
    search_fields = ('title', 'message')
    fields = ('first_name', 'last_name', 'phone', 'email', 'title', 'message', "created_at")
    readonly_fields = ('first_name', 'last_name', 'title',
                       'message', 'phone', 'email', "created_at")


admin.site.register(Feedback, ContactAdmin)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
    fields = ('email', 'date')
    readonly_fields = ('email', "date")


