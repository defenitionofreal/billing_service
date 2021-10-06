from .default import *
import os


DEBUG = eval(os.environ.get('DEBUG', 'True'))

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'
