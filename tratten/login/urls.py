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

urlpatterns = patterns('',

    # Login
    url(_(r'^$'),
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name="login"),
    url(_(r'^new-password/$'),
        'django.contrib.auth.views.password_reset',
        {'template_name': 'password-reset-form.html',
         'email_template_name': 'password-reset-email.html'},
        name="password-reset"),
    url(_(r'^new-password/sent/$'),
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'password-reset-done.html'},
        name="password-reset-done"),
    url(_(r'^new-password/complete/$'),
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'password-reset-complete.html'},
        name="password-reset-complete"),
    url(_(r'^new-password/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+?)/$'),
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'password-reset-confirm.html'},
        name="password-reset-confirm"),

)

# Switch back to the language of choice
translation.activate(language_saved)
