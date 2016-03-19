from django.contrib import admin
from .models import Notice, Board, Product

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'updated_date', 'photo')
admin.site.register(Notice, NoticeAdmin)

class BoardAdmin(admin.ModelAdmin):
	list_display = ('title', 'updated_date', 'upload')
admin.site.register(Board, BoardAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'image', 'image_url')
admin.site.register(Product, ProductAdmin)
