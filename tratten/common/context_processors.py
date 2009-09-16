#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site


def site(request):
    """Return information about current site."""

    # TODO: Figure out if caching is necessary for 1.0 (see below)
    # http://docs.djangoproject.com/en/dev/ref/contrib/sites/ \
    #                                      #caching-the-current-site-object
    # site_name = cache_get('site_name')
    # if not site_name:
    site_name = Site.objects.get_current().name
    #cache.set('site_name', site_name, 24*3600)

    return {"site_name": site_name}
