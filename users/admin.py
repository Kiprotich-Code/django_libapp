from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = StaffRegisterForm
    form = StudentRegisterForm
    model = CustomUser
    list_display = ("email", "full_names", 'user_type', "is_active",)
    list_filter = ("email", "full_names", "user_type", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "full_names", "user_type", "admission_no", "staff_id", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "staff_id", "admission_no", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)