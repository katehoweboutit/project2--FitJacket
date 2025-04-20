from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FitUser
from .forms import FitUserCreationForm #new
from django.contrib.auth.forms import UserChangeForm #new

# Register your models here.
class FitUserAdmin(UserAdmin):
    add_form = FitUserCreationForm #new
    form = UserChangeForm #new
    model = FitUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'age', 'weight', 'fit_points']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'age', 'weight', 'fit_points']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'age', 'weight', 'fit_points', 'Lifestyle_Habits', 'Additional_Notes')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff')}
        ),
    )
    actions = ['add_friend']
    def add_friend(self, request, queryset):
        for friend in queryset:
            #add to this user's list of friends
            friend.save()

admin.site.register(FitUser, FitUserAdmin)