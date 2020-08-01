from django.contrib import admin
from .models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['author']
    fields = ['author', 'email', 'text', 'created_at', 'updated_at']


admin.site.register(GuestBook, GuestBookAdmin)

