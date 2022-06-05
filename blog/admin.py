from django.contrib import admin
from .models import Post
 
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "date_of_post", "data_of_change"]
    list_display_links = ["id", "date_of_post"]
    list_editable = ["title"]
    list_filter = ["date_of_post", "data_of_change"]
    search_fields = ["title", "description"]
    class Meta:
        model = Post
 
admin.site.register(Post, PostModelAdmin)
