from django.contrib import admin
from django.db import models

from ..enums import ArticleStatus
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'articles_count',
        'published_count',
    ]

    search_fields = [
        'title',
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            articles_count=models.Count(
                'articles',
                filter=models.Q(
                    articles__status=ArticleStatus.PUBLISHED,
                ),
            ),
            published_count=models.Count(
                'articles',
                filter=models.Q(
                    articles__status=ArticleStatus.PUBLISHED,
                ),
            ),
        )

    def articles_count(self, obj: Category):
        return obj.articles_count

    articles_count.short_description = 'Всего статей'
    articles_count.admin_order_field = 'articles_count'

    def published_count(self, obj: Category):
        return obj.published_count

    published_count.short_description = 'Всего опубликовано'
    published_count.admin_order_field = 'published_count'
