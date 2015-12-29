from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i1yypfxi_&du3suchi+3rw_#swyz00y-gph*$^z-=ol60c8&(5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
