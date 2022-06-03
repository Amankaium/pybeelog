from django.contrib import admin

# Register your models here.
from .models import Feedback, OurContact, Subscribe


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone', 'title', 'checked', "created_at")
    list_display_links = ('id', 'title')
    search_fields = ('title', 'message',)
    list_editable = ('checked',)
    list_filter = ('checked',)
    fields = ('first_name', 'last_name', 'phone', 'email', 'title', 'message', "created_at",
              'checked')
    readonly_fields = ('first_name', 'last_name', 'title',
                       'message', 'phone', 'email', "created_at")


admin.site.register(Feedback, ContactAdmin)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
    fields = ('email', 'date')
    readonly_fields = ('email', "date")


@admin.register(OurContact)
class OurContact(admin.ModelAdmin):
    list_display = ("title", "description", "description2")
    fields = ("title", "description", "description2")
