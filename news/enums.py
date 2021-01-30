from django.db.models import IntegerChoices


class ArticleStatus(IntegerChoices):

    DRAFT = 0, 'Черновик'
    PUBLISHED = 1, 'Опубликована'
