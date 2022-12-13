from django.contrib import admin

# Register your models here.
from .models import Post # this the post class from models.py

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",) # lets you filter
    search_fields = ['title', 'content'] # lets you search using the title and content field
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)