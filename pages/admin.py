from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

class AdminPost(SummernoteModelAdmin):
    list_display = ['title', 'author', 'status', 'created_date']
    summernote_fields = ('description')

admin.site.register(Post, AdminPost)
admin.site.register(Author)
admin.site.register(Category)


class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_date']

admin.site.register(Contact, AdminContact)


class AdminComment(admin.ModelAdmin):
    list_display = ['name', 'is_approved', 'created_date']

admin.site.register(Comment, AdminComment)

