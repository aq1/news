from django.http import Http404
from django.shortcuts import (
    render,
    get_object_or_404,
)

from ..models import Article


def article(request, slug):
    try:
        article = get_object_or_404(Article.objects.published(), id=slug.split('-')[0])
    except ValueError:
        raise Http404()
    context = {
        'article': article
    }
    return render(request, 'news/article.html', context)
