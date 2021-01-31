from django.db import models


class Category(models.Model):

    title = models.CharField(
        max_length=64,
        verbose_name='Название',
    )

    slug = models.SlugField(
        verbose_name='URL путь',
        help_text='Отображается в адресной строке',
        default='',
        blank=True,
    )

    class Meta:
        default_related_name = 'categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
