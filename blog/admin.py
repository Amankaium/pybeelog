from django.contrib import admin
from .models import Post
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'posts_text')
    list_display_links = ('title',)