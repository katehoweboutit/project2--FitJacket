from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FitUser

# Register your models here.
class FitUserAdmin(UserAdmin):
    model = FitUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'age', 'weight']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'age', 'weight']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'weight', 'LifestyleHabits', 'AdditionalNotes')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(FitUser, FitUserAdmin)