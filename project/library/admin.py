from django.contrib import admin

from .models import Book


@admin.register(Book)
class ProjectAdmin(admin.ModelAdmin):
    """ Spécifications for administration of projects """
    list_display = [
        "title", "author",
        "created_time", "updated_time"
        ]
    list_filter = ["created_time", "updated_time"]
    search_fields = ["title"]
    ordering = ["-created_time"]
