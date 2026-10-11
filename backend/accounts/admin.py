from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'role', 
        'shop', 
        'is_staff'
    )
    list_filter = ('role', 'shop', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    
    # Include role, shop, and phone_number in Django Admin edit forms
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Shop & Role Settings', {'fields': ('role', 'shop', 'phone_number')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Shop & Role Settings', {'fields': ('role', 'shop', 'phone_number')}),
    )