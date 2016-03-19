from django.contrib import admin
from .models import Post, Comment

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'created_date')
admin.site.register(Post, AdminPost)

admin.site.register(Comment)
