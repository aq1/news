from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

admin.site.unregister(User)


class UserAddForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserAddForm

    list_filter = [
        'is_staff',
    ]

    list_display = [
        'username',
        'full_name'
    ]

    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'first_name',
                'last_name',
                'username',
                'password1',
                'password2',
            ),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and obj.is_superuser:
            return [
                'username',
                'password',
                'first_name',
                'last_name',
            ]

        return super().get_readonly_fields(request, obj)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)

        return (
            (None, {
                'fields': (
                    'username',
                    'password',
                    'first_name',
                    'last_name',
                ),
            }),
        )

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fields(request, obj)

        if obj.is_superuser:
            return []

        return [
            'username',
            'password',
            'first_name',
            'last_name',
        ]

    def full_name(self, obj: User):
        return f'{obj.first_name} {obj.last_name}'

    full_name.short_description = 'Полное имя'
    full_name.admin_order_field = 'last_name'

    def is_author(self, obj: User):
        return obj.is_staff

    is_author.short_description = 'Автор?'
    is_author.boolean = True
