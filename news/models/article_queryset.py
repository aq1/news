from django.contrib.postgres.search import (
    SearchRank,
    SearchVector,
)
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

    def search(self, search_query):
        vector = (
            SearchVector('title', weight='A')
            + SearchVector('description', weight='B')
            + SearchVector('body_text', weight='C')
        )
        return self.annotate(
            rank=SearchRank(
                vector,
                search_query,
            ),
        ).order_by(
            '-rank',
        ).exclude(
            rank__lte=0.2,
        )
