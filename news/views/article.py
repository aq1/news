from django.shortcuts import (
    render,
    get_object_or_404,
)

from ..models import Article
from ..models import Comment


def article(request, article_id, slug=None):
    qs = Article.objects.with_author()
    if not request.user.is_superuser:
        qs = qs.published()

    context = {
        'article': get_object_or_404(qs, id=article_id),
        'comments': Comment.objects.select_related(
            'author',
        ).filter(
            article_id=article_id,
        ).order_by(
            '-created_at',
        )[:10],
    }

    return render(request, 'news/article.html', context)
