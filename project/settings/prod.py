from .default import *
import os

DEBUG = os.environ['DJANGO_DEBUG']


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

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.environ['REDIS_URI']],
        },
    },
}

CELERY_BROKER_URL = os.environ['BROKER_URL']
