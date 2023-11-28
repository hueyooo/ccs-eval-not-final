from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.apps import apps

class CustomUserAdmin(UserAdmin):
  list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff',
    'image', 'role'
  )

  fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('image', 'role')
        })
  )

  add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('image', 'role')
        })
  )

admin.site.register(User, CustomUserAdmin)

main_models = apps.get_app_config('main').get_models()

for model in main_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass