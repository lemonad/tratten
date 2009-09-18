#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
import posix

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '/')

# Moved to local_settings:
#
# ADMINS = (
#     ('admin', 'admin@example.com'),
# )
#
# MANAGERS = ADMINS

# Moved to production, development and local_settings:
#
# DATABASE_ENGINE = ''      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_NAME = ''
# DATABASE_USER = ''        # Not used with sqlite3.
# DATABASE_PASSWORD = ''    # Not used with sqlite3.
# DATABASE_HOST = ''        # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''        # Set to empty string for default. Not used with sqlite3.

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
SECRET_KEY = 'use-local-settings-py-to-set-this-to-something-else'

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

# The below LOGIN_URL and LOGOUT_URL doesn't seem to be used except
# when unit testing views.
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'

EMAIL_SUBJECT_PREFIX = "Tratten: "
DEFAULT_FROM_EMAIL = "do-not-reply@example.com"
SERVER_EMAIL = "do-not-reply@example.com"
# EMAIL_HOST = "localhost"
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""


#
# Settings for email backend (also see local settings)
#
EMAIL_BACKEND_ENABLED = True

#
# Settings for Mantis issue list backend (also see local settings)
#
# Observe that CSV Export columns are 1-based
#
#
# Mantis Standard (English):
#
# Id, Project, Reporter, Assigned To, Priority, Severity, Reproducibility,
# Product Version, Projection, Date Submitted, ETA, OS, OS Version, Platform,
# View Status, Updated, Summary, Status, Resolution, Fixed in Version
#
MANTIS_ISSUE_LIST_BACKEND_ENABLED = True

MANTIS_ISSUE_LIST_BACKEND_ID_NAME = "Id"
MANTIS_ISSUE_LIST_BACKEND_ID_COL = 1
MANTIS_ISSUE_LIST_BACKEND_PROJECT_NAME = "Project"
MANTIS_ISSUE_LIST_BACKEND_PROJECT_COL = 2
MANTIS_ISSUE_LIST_BACKEND_ASSIGNED_TO_NAME = "Assigned To"
MANTIS_ISSUE_LIST_BACKEND_ASSIGNED_TO_COL = 4
MANTIS_ISSUE_LIST_BACKEND_DATE_SUBMITTED_NAME = "Date Submitted"
MANTIS_ISSUE_LIST_BACKEND_DATE_SUBMITTED_COL = 11
MANTIS_ISSUE_LIST_BACKEND_SUMMARY_NAME = "Summary"
MANTIS_ISSUE_LIST_BACKEND_SUMMARY_COL = 18
MANTIS_ISSUE_LIST_BACKEND_STATUS_NAME = "Status"
MANTIS_ISSUE_LIST_BACKEND_STATUS_COL = 19

MANTIS_ISSUE_LIST_BACKEND_USE_PROJECT = "example"
MANTIS_ISSUE_LIST_BACKEND_FILTER_ON_COL_NAME = "entity"
