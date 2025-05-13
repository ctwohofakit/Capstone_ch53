from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter  = ("is_staff", "is_active", "is_superuser", "groups")


    fieldsets = (
        (None,{"fields": ("email", "password")}),
        ("Personal Info",{"fields": ("first_name", "last_name")}),
        ("Permissions",{"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates",{"fields": ("last_login", "date_joined")}),
    )


    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(Account, AccountAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "country")
    search_fields = ("user__email", "city", "state", "country")
