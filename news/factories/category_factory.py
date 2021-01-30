import factory
from faker import Faker

from ..models import Category

fake = Faker('ru-RU')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(lambda n: fake.word())
