from django.contrib import admin

# Register your models here.
from post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    list_filter = ['author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'date_created']
    list_filter = ['post']