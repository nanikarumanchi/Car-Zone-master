from django.contrib import admin

from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car']
    search_fields = ['id', 'user', 'car']
    list_filter = ['car', 'user', 'state', 'created_at']
    raw_id_fields = ['car', 'user']
