from django.shortcuts import render

from ..models import Article


def index(request):
    context = {
        'articles': Article.objects.select_related(
            'category',
        ).with_author().published()[:15]
    }
    return render(request, 'news/index.html', context)
