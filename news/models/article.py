from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from model_utils.fields import MonitorField
from unidecode import unidecode
from bs4 import BeautifulSoup

from ..enums import ArticleStatus
from .article_queryset import ArticleQuerySet


class Article(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name='Автор статьи',
        null=True,
    )

    category = models.ForeignKey(
        'news.Category',
        on_delete=models.SET_NULL,
        related_name='articles',
        verbose_name='Категория',
        null=True,
    )

    title = models.CharField(
        max_length=1024,
        verbose_name='Заголовок',
    )

    description = models.TextField(
        verbose_name='Короткое описание',
        help_text='Будет отображено под заголовком',
        default='',
        blank=True,
    )

    slug = models.SlugField(
        verbose_name='URL статьи',
        help_text='Отображается в адресной строке',
        editable=False,
        max_length=100,
    )

    cover = models.ImageField(
        upload_to='covers',
        null=True,
        blank=True,
    )

    published_at = MonitorField(
        'Дата публикации',
        monitor='status',
        when=[ArticleStatus.PUBLISHED],
        null=True,
        default=None,
    )

    status = models.PositiveSmallIntegerField(
        verbose_name='Статус',
        choices=ArticleStatus.choices,
        default=ArticleStatus.DRAFT,
    )

    body = RichTextUploadingField(
        verbose_name='Текст статьи',
        default='',
        blank=True,
    )

    body_text = models.TextField(
        default='',
        editable=False,
    )

    objects = ArticleQuerySet.as_manager()

    class Meta:
        default_related_name = 'articles'
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Статья {self.title}'

    def save(self, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.body_text = BeautifulSoup(self.body, 'html.parser').text
        super().save(**kwargs)

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        return ''

    @property
    def is_draft(self):
        return self.status == ArticleStatus.DRAFT
