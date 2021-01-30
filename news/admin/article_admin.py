from django.contrib import admin

from ..enums import ArticleStatus
from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'is_published',
        'published_at',
    ]

    readonly_fields = [
        'slug',
        'published_at',
    ]

    list_select_related = [
        'author',
        'category',
    ]

    search_fields = [
        'title',
    ]

    autocomplete_fields = [
        'author',
        'category',
    ]

    def is_published(self, obj: Article):
        return obj.status == ArticleStatus.PUBLISHED

    is_published.short_description = 'Опубликована?'
    is_published.admin_order_field = 'status'
    is_published.boolean = True
