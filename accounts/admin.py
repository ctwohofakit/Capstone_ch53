from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile

# 1) A custom UserAdmin that works with your email-as-username model
class AccountAdmin(UserAdmin):
    model = Account

    # show these columns in the user list
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter  = ("is_staff", "is_active", "is_superuser", "groups")

    # these panels and fields appear on the edit-user page
    fieldsets = (
        (None,               {"fields": ("email", "password")}),
        ("Personal Info",    {"fields": ("first_name", "last_name")}),
        ("Permissions",      {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates",  {"fields": ("last_login", "date_joined")}),
    )

    # when you click “Add user” in the admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering      = ("email",)

# 2) Register your Account using the custom admin
admin.site.register(Account, AccountAdmin)

# 3) Register your UserProfile with a simple ModelAdmin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "country")
    search_fields = ("user__email", "city", "state", "country")
