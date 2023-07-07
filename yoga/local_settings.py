import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8@0233=to9z2)x5ymsmyk8g*k25+ka9tp!-m3-8g81ylwq+syk'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hello_django_dev',
        'USER': 'hello_django',
        'PASSWORD': 'hello_django',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


STATICFILES_DIRS = [os.path.join('static'), ]
