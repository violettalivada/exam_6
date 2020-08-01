from django.contrib import admin
from .models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['author', 'email', 'text']


admin.site.register(GuestBook, GuestBookAdmin)

