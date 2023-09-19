from django.contrib import admin
from django.utils.html import format_html

from .models import Car
# Register your models here.


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.car_photo.url}" style="border-radius: 10px" width="50" />')
    thumbnail.short_description = "CAR IMAGE"
    list_display = ['id', 'thumbnail', 'title',
                    'state', 'city', 'year', 'price', 'is_featured', ]
    search_fields = ['id', 'title', 'year', 'description', ]
    list_editable = ['is_featured', ]
    list_filter = ['year', 'created_date']
