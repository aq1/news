from django.contrib import admin

from ..models import UserFeedback


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user',
        'email',
    ]
