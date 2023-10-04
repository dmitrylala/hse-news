from django.contrib import admin

from .models import (
    News,
    Page,
)

admin.site.register(News)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.get_fields()]
    list_display_links = ["title"]
    list_editable = ["navig", "navig_position", "context_type", "content"]
    search_fields = ["content"]
    list_filter = ["title", "navig", "context_type"]
