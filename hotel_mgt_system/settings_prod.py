
from .settings import *
import dj_database_url

#override
DEBUG = True


ALLOWED_HOSTS = ['noble-hms.herokuapp.com']

#postgres database for production

DATABASES = {}
DATABASES['default'] = dj_database_url.config()