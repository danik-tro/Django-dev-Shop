from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomAdmin(UserAdmin):
    fieldsets = (("User", {"fields": ("image",)}),) + UserAdmin.fieldsets


admin.site.register(User, CustomAdmin)
