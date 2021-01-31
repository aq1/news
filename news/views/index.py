from django.http import Http404
from django.shortcuts import render

from ..models import Article


def index(request, category_slug=None):

    qs = Article.objects.with_author()

    _preview = request.GET.get('preview')

    if not (_preview and request.user.is_superuser):
        qs = qs.published()

    if category_slug:
        qs = qs.filter(category__slug=category_slug)

    context = {
        'articles': qs[:15],
        'preview': _preview,
    }

    return render(request, 'news/index.html', context)
