from django.contrib import admin
from .models import *

# Register your models here.


class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description',)


admin.site.register(Faq, FaqAdmin)


class FaqFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title',
                    'email', 'created_at', 'checked')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'message', 'created_at')
    list_editable = ('checked',)
    list_filter = ('checked', 'created_at')
    fields = ('name', 'email', 'phone', 'title', 'message', 'created_at',
              'checked')
    readonly_fields = ('name', 'email', 'title',
                       'message', 'phone', "created_at")


admin.site.register(FaqFeedback, FaqFeedbackAdmin)
