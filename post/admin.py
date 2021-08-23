from django.contrib import admin

# Register your models here.
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']