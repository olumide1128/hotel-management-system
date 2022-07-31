
from .settings import *

#override
DEBUG = True

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'hms',
       'USER': 'postgres',
       'PASSWORD': 'olupostgresql94',
       'HOST': 'localhost',
       'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']