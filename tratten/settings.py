#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
import posix

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# logging.basicConfig(
#     level = logging.DEBUG,
#     format = '%(asctime)s %(levelname)s %(message)s',
#     filename = '/tmp/tratten.log',
#     filemode = 'w'
# )

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '/')

ADMINS = (
    ('jnt', 'jonasnockert@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'tratten.db'
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Europe/Stockholm'

LANGUAGE_CODE = 'sv-SE'
# LANGUAGE_CODE = 'en-US'

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('sv', ugettext('Swedish')),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Don't share this with anybody.
SECRET_KEY = '23094820398ehsfjkjsdhfsdfo8wy8ryw3r09ywh3roihw3krgwi3ur'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'djangoflash.middleware.FlashMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'tratten.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'south',
    'tratten.categories',
    'tratten.common',
    'tratten.errorreports',
    'tratten.flatcontent',
    'tratten.issues',
    'tratten.login',
    'tratten.preferences',
)

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'tratten.common.context_processors.site',
    'djangoflash.context_processors.flash',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

FIXTURE_DIRS = (
    os.path.join(os.path.dirname(__file__), "categories/fixtures"),
    os.path.join(os.path.dirname(__file__), "common/fixtures"),
    os.path.join(os.path.dirname(__file__), "flatcontent/fixtures"),
    os.path.join(os.path.dirname(__file__), "issues/fixtures"),
)

SITE_ID = 1

DEFAULT_FROM_EMAIL = "jonasnockert@gmail.com"
SERVER_EMAIL = "jonasnockert@gmail.com"
EMAIL_SUBJECT_PREFIX = "Tratten: "

# The below LOGIN_URL and LOGOUT_URL doesn't seem to be used except
# when unit testing views.
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'
