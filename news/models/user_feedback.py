from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from model_utils.fields import MonitorField
from unidecode import unidecode
from bs4 import BeautifulSoup

from ..enums import ArticleStatus
from .article_queryset import ArticleQuerySet


class UserFeedback(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь',
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        default='',
    )

    email = models.EmailField(
        verbose_name='Email',
    )

    body = models.TextField(
        verbose_name='Текст сообщения',
    )

    class Meta:
        default_related_name = 'feedbacks'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения от пользователей'

    def __str__(self):
        return f'Сообщение от {self.name}'
