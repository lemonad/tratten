#!/usr/bin/python
# -*- coding: utf-8 -*-

from tratten.settings import *

DEBUG=True
TEMPLATE_DEBUG=DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tratten.db'

try:
    from tratten.local_settings import *
except ImportError:
    pass
