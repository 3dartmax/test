from django.contrib import admin
from .models import Author, Book

class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'title', 'birth_date')
admin.site.register(Author, AdminAuthor)
admin.site.register(Book)
