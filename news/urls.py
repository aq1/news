from django.urls import (
    path,
)

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>-<path:path>', views.article, name='article'),
]
