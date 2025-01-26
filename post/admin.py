from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets  # You don't need to add custom fields here

    list_display = UserAdmin.list_display + ('get_groups',)  # Add 'get_groups' to list_display

    # Method to display the user's groups in the list view
    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Grupo'

admin.site.unregister(User)  
admin.site.register(User, CustomUserAdmin)