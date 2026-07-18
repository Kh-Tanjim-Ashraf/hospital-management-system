from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from account.models import User_Profile


User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'role', 'is_active', 'is_superuser']

    list_display_links = ['id', 'email']

    list_filter = ['is_active', 'role', 'is_superuser']

    search_fields = ['id', 'email', 'role']

    ordering = ['id', 'email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "role",
                "password1",
                "password2",
            ),
        }),



admin.site.register(User_Profile)