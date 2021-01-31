from django.shortcuts import render

from ..models import Article


def index(request, preview=None):

    qs = Article.objects.with_author()
    if not (preview and request.user.is_superuser):
        qs = qs.published()

    context = {
        'articles': qs[:15],
        'preview': preview,
    }

    return render(request, 'news/index.html', context)


def preview(request):
    return index(request, True)
