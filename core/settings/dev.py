from core.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_value('DATABASE_NAME'),
        'USER': get_env_value('DATABASE_USERNAME'),
        'PASSWORD': get_env_value('DATABASE_PASSWORD'),
        'HOST': 'database',
        'PORT': '',
    }
}