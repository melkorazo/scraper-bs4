import platform
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.getenv('API_DB_NAME', 'db.sqlite3')),
    }
}

INSTALLED_APPS = ['data']

TIME_ZONE = 'America/Santiago'

LANGUAGE_CODE = 'es-cl'

SECRET_KEY = 't}Fii=A-2s\VWg;>mvowQ,w(.+P,3C1b?(wx-6KM(PhrzLS%'

DEBUG = os.getenv('DEBUG', True)

USE_I18N = True

USE_L10N = True

USE_TZ = True

APP_NAME = 'data'

LOG_MAXSIZE = 102400

LOG_MAXFILES = 5

HOSTNAME = platform.node()
