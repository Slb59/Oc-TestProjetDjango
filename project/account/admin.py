from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """ Spécifications for administration of users """
    list_display = [
        'username', 'date_joined', 'is_staff', 'birth_date'
        ]
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {"fields": [
            "birth_date",
            "can_be_contacted", "can_data_be_shared"
            ]}),)
    add_fieldsets = auth_admin.UserAdmin.add_fieldsets + (
        (None, {"fields": [
            'brith_date',
            "can_be_contacted", "can_data_be_shared"
            ]}),)
