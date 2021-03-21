import datetime

from django import forms
from django.db import DatabaseError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from ..models import UserFeedback


class WriteUsForm(forms.Form):
    email = forms.EmailField(
        required=True,
    )

    name = forms.CharField(
        required=True,
        max_length=100,
    )

    body = forms.CharField(
        max_length=10000,
        required=True,
    )


@require_http_methods(['post'])
def write_us(request):
    now = datetime.datetime.now()
    try:
        last_request_time = datetime.datetime.fromisoformat(request.session['write_us_last_request'])
    except (KeyError, ValueError):
        last_request_time = datetime.datetime(2020, 1, 1)

    if (now - last_request_time).total_seconds() < 5:
        return JsonResponse({}, status=429)

    form = WriteUsForm(request.POST)

    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    user = request.user
    if user.is_anonymous:
        user = None

    try:
        UserFeedback.objects.create(
            user=user,
            **form.cleaned_data,
        )
    except DatabaseError:
        return JsonResponse({}, status=400)

    request.session['write_us_last_request'] = now.isoformat()
    return JsonResponse({}, status=201)
