from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )

    article = models.ForeignKey(
        'news.Article',
        on_delete=models.CASCADE,
        verbose_name='Статья',
    )

    body = models.TextField(
        verbose_name='Текст комментария',
        max_length=3000,
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий к {self.article} от {self.author}'
