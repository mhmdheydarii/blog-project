from django.contrib import admin
from .models import *

class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_date']

admin.site.register(Post, AdminPost)
admin.site.register(Author)
admin.site.register(Catgory)