import random

import factory
from django.utils import timezone
from faker import Faker

from django.contrib.auth import get_user_model

from ..enums import ArticleStatus
from ..models import Article, Category

fake = Faker('ru-RU')


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    description = factory.Sequence(lambda n: fake.text(random.randint(10, 40)))
    body = factory.Sequence(lambda n: fake.text(1000))
    status = ArticleStatus.PUBLISHED

    @factory.post_generation
    def generate_slug(obj: Article, create, extracted, **kwargs):
        obj.save()

    @factory.lazy_attribute
    def title(self):
        return ' '.join(fake.text().split()[:random.randint(4, 7)])

    @factory.lazy_attribute
    def category(self):
        return random.choice(Category.objects.all())

    @factory.lazy_attribute
    def published_at(self):
        return timezone.now()

    @factory.lazy_attribute
    def author(self):
        return random.choice(get_user_model().objects.all())
