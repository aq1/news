from django.shortcuts import render

from ..models import Article


def index(request, category_slug=None):

    qs = Article.objects.with_author()

    _preview = request.GET.get('preview')

    if not (_preview and request.user.is_superuser):
        qs = qs.published()

    if category_slug:
        qs = qs.filter(category__slug=category_slug)

    search_query = request.GET.get('q', '')
    if search_query:
        qs = qs.search(search_query=search_query)

    context = {
        'articles': qs[:11],
        'preview': _preview,
        'search': search_query,
    }

    return render(request, 'news/index.html', context)
