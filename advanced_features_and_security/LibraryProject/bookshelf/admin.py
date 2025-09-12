from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , Book


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active")}
        ),
    )
    
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")