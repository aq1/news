from django.db import models
from django.db.models import functions
from ..enums import ArticleStatus


class ArticleQuerySet(models.QuerySet):

    def with_author(self):
        return self.select_related(
            'author',
            'category',
        ).annotate(
            author_name=functions.Concat(
                'author__first_name',
                models.Value(' '),
                'author__last_name',
            ),
        ).order_by(
            '-published_at',
        )

    def published(self):
        return self.filter(
            status=ArticleStatus.PUBLISHED,
        )
