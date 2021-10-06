from .default import *
import os

DEBUG = eval(os.environ.get('DEBUG', 'True'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}