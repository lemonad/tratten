#!/usr/bin/python
# -*- coding: utf-8 -*-

from tratten.settings import *

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'tratten'
DATABASE_USER = 'tratten'
# DATABASE_HOST = ''        # Set to empty string for localhost.
# DATABASE_PORT = ''        # Set to empty string for default.

try:
    from tratten.local_settings import *
except ImportError:
    pass
