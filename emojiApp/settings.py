DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import os
    SECRET_KEY = os.environ['SECRET_KEY']

    import django_heroku
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

    django_heroku.settings(locals(), staticfiles=False)
