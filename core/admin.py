from django.contrib import admin
from .models import Guest, Gift

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_chosen')
    list_filter = ('is_chosen',)
    search_fields = ('name',)
