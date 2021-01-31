from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

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
        'preview',
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

    def preview(self, obj: Article):
        url = reverse('news:article', kwargs={'slug': obj.slug})
        return mark_safe(
            f'<a href={url}>Посмотреть как будет выглядеть на сайте</a>'
        )

    preview.short_description = 'Превью'
