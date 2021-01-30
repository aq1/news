from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from model_utils.fields import MonitorField

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

    objects = ArticleQuerySet.as_manager()

    class Meta:
        default_related_name = 'articles'
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Статья {self.title}'

    def save(self, **kwargs):
        slug = slugify(self.title, allow_unicode=True)

        if self.id:
            slug = f'{self.id}-{slug}'
        else:
            slug = f'0-{slug}'

        self.slug = slug
        return super().save(**kwargs)

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        return ''
