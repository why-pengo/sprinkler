# https://pipenv.readthedocs.io/en/latest/advanced/#automatic-loading-of-env
# PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell
# Let's see if we can get django-environ and pipenv to play together

import os
import environ
root = environ.Path(__file__) - 3  # three folders back (/a/b/c/ - 3 = /)
env = environ.Env(  # set default values and casting
    DEBUG=(bool, False),
)
environ.Env.read_env()  # reading .env file

DEBUG = env('DEBUG')  # False if not in os.environ
TEMPLATE_DEBUG = DEBUG
BASE_DIR = root()  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'scheduler',
    'status'
]

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'controller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/jinja2'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'controller.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/dtl'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'controller.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = 'public/'
# STATIC_URL = '/static/'
STATIC_URL = '/public/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# https://docs.djangoproject.com/en/2.1/topics/http/sessions/#browser-length-vs-persistent-sessions
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 28800  # 8h in seconds
# https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-clearsessions
