#!/usr/bin/python
# -*- coding: utf-8 -*-

from tratten.settings import *

DEBUG=True
TEMPLATE_DEBUG=DEBUG

try:
    from tratten.local_settings import *
except ImportError:
    pass
