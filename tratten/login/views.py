#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect)
from django.template import Context, RequestContext, loader
from django.utils.translation import ugettext, ugettext_lazy as _


#
# Views
#


def logout_view(request):
    """Logs out."""

    logout(request)

def login_view(request):
    """Logs in."""

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        # Return an 'invalid login' error message.
        # TODO: Must fix broken redirect
        return HttpResponseRedirect('login-error.html')
    else:
        if user.is_active:
            login(request, user)
        else:
            # Return a 'disabled account' error message
            # TODO: Must fix broken redirect
            return HttpResponseRedirect('account-disabled.html')
