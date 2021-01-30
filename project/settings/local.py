from .base import *  # noqa

DEBUG = True
SECRET_KEY = '-@4w7rdgkqb_wbzfi#hom&55=(#w(x6f7qh-5!qbzadkjko3p9'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
