import os
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emojiApp',
    'bootstrap4',
    'crosslingual.apps.CrosslingualConfig',
    'emojiTransApp.apps.EmojitransappConfig',
    'paper.apps.PaperConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emojiApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'emojiApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR + "/logs/django.log",
#             "formatter": "verbose",
#             "maxBytes": 1024 * 1024 * 1,
#             "backupCount": 5,
#         },
#     },
#     "formatters": {
#         "verbose": {
#             "format": "\t".join(
#                 [
#                     "[%(levelname)s]",
#                     "%(asctime)s",
#                     "%(name)s.%(funcName)s:%(lineno)s",
#                     "%(message)s",
#                 ]
#             )
#         },
#     },
#     "loggers": {
#         "file": {
#             "handlers": ["file"],
#             "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
#             "propagate": True,
#         },
#     },
# }

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#テンプレートなどでwebサーバーが探しに行く場所
STATIC_URL = '/static/'

# staticファイルを集約する場所
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#プロジェクト全体に共通するstaticファイル
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
