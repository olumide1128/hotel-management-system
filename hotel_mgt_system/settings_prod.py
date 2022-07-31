
from .settings import *
import dj_database_url

#override
DEBUG = True


ALLOWED_HOSTS = ['noble-hms.herokuapp.com']

#postgres database for production
db_from_env = dj_database_url.config()
DATABASES = {}
DATABASES['default'].update(db_from_env)