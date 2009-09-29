#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader


#
# Views
#


def select_language(request):
    """Select prefered site language via a form (i18n)."""

    t = loader.get_template('select_language.html')
    c = RequestContext(request, {
        })
    return HttpResponse(t.render(c))
