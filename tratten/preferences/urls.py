#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include, handler500, url
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.utils.translation import ugettext as _

# Switch language temporarily for "static" I18n of URLs
language_for_urls = settings.LANGUAGE_CODE[:2]
language_saved = translation.get_language()
translation.activate(language_for_urls)

urlpatterns = patterns('tratten.preferences.views',
    # Language
    url(_(r'^language/$'), 'select_language', name='select-language'),
    )

# Switch back to the language of choice
translation.activate(language_saved)
