from .base import *

ALLOWED_HOSTS = []

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_blog',
        'USER': 'root',
        'PASSWORD': 'info25',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}