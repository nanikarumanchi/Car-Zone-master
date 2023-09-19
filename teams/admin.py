from django.contrib import admin
from django.utils.html import format_html

from .models import Team


@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.image.url}' style='border-radius: 50px;' width='40' />")
    thumbnail.short_description = 'PROFILE IMAGE'
    list_display = ['id', 'thumbnail',
                    '__str__', 'designation', 'created_date']
    search_fields = ['id', 'first_name', 'last_name', 'designation']
    list_display_links = ['id', '__str__']
    date_hierarchy = 'created_date'
