# encoding:utf-8

"""
Django settings for quantvc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mtc+bud&+a5lw*tk^kxai%9+6mu_37yy8w*^0sb-w3voya_7#='

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# https://docs.djangoproject.com/en/1.7/ref/contrib/sites/#enabling-the-sites-framework
SITE_ID = 1

ALLOWED_HOSTS = []


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('zh-cn', u'中文'),
    ('en', u'English'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    # django allauth
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATION_BACKENDS = (
    # django userena
    'userena.backends.UserenaAuthenticationBackend',
    # django guardian
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Application definition
INSTALLED_APPS = (
    'django.contrib.sites',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.formtools',
)

EXTENSION_APPS = (
    "django_extensions",
    "easy_thumbnails",
    "guardian",
    "userena",
    "userena.contrib.umessages",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "django_filters",
    "taggit",
    "crispy_forms",
    "imagekit",
    "django_rq",
    "djangosecure",
    "rosetta",

    # 'mptt',
)

WEB_APPS = (
    'accounts',  # can't put accounts in the apps!!!
    'apps.web',
)

INSTALLED_APPS += (EXTENSION_APPS + WEB_APPS)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "djangosecure.middleware.SecurityMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'quantvc.urls'

WSGI_APPLICATION = 'quantvc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "quantvc",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "1qaz",
        "OPTIONS": {
            "init_command": "SET storage_engine=INNODB",
        },
        "TEST": {
            'CHARSET': "utf8",
            'COLLATION': "utf8_general_ci",
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "static_files"),
)

# date time
DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i:s"

# FILE
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440

# Template dirs
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# email
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "rq_console": {
            "format": "%(asctime)s %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        "rq_console": {
            "level": "DEBUG",
            "class": "rq.utils.ColorizingStreamHandler",
            "formatter": "rq_console",
            "exclude": ["%(asctime)s"],
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        "rq.worker": {
            "handlers": ["rq_console"],
            "level": "DEBUG"
        },
    }
}

# security
# TODO: bugs! If set True , can't login the admin!
SESSION_COOKIE_SECURE = False


