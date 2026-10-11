from django.contrib import admin
from .models import Shop

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'address', 
        'latitude', 
        'longitude', 
        'geofence_radius', 
        'is_active', 
        'created_at'
    )
    list_filter = ('is_active',)
    search_fields = ('name', 'address')