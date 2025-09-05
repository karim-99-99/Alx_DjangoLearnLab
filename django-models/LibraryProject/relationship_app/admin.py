
# Register your models here.
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')   # show user and role in list
    list_filter = ('role',)           # filter by role in sidebar
    search_fields = ('user__username',)  # search by username
