from django.contrib.auth.decorators import login_required
from django.db import DatabaseError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from ..models import Comment


@login_required
@require_http_methods(['POST'])
def comment(request, article_id):
    body = request.POST.get('body')
    if not body:
        return JsonResponse({}, status=400)

    try:
        _comment = Comment.objects.create(
            article_id=article_id,
            body=body,
            author=request.user,
        )
    except DatabaseError:
        return JsonResponse({}, status=400)

    return JsonResponse({}, status=201)
