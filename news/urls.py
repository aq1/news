from django.urls import (
    path,
)

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('write-us', views.write_us, name='write_us'),
    path('post-comment', views.write_us, name='post_comment'),
    path('<int:article_id>-<slug:slug>', views.article, name='article'),
    path('<str:category_slug>', views.index, name='category'),
]
