from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_done', 'created_at']
    list_filter = ['is_done']
    search_fields = ['title', 'description']
