from django.http import Http404
from django.shortcuts import (
    render,
    get_object_or_404,
)

from ..models import Article


def article(request, article_id, path=None):
    qs = Article.objects.all()
    if not request.user.is_superuser:
        qs = qs.published()

    try:
        _article = get_object_or_404(qs, id=article_id)
    except ValueError:
        raise Http404()
    context = {
        'article': _article
    }
    return render(request, 'news/article.html', context)
