from django.contrib import admin
from main.models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'create_time', 'category']
    list_filter = ['create_time', 'category']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)