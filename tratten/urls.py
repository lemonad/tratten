from django.conf import settings
from django.conf.urls.defaults import (patterns, include, handler404,
                                       handler500, url)
from django.contrib import admin
from django.utils import translation
from django.utils.translation import ugettext as _


admin.autodiscover()

handler404
handler500

# Switch language temporarily for "static" I18n of URLs
language_for_urls = settings.LANGUAGE_CODE[:2]
language_saved = translation.get_language()
translation.activate(language_for_urls)

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # Issues
    url(_(r'^$'), 'tratten.issues.views.index', name="index"),
    url(_(r'^create$'), 'tratten.issues.views.create', name="create-issue"),
    url(_(r'^list$'), 'tratten.issues.views.list', name="list-issues"),
    url(_(r'^done$'), 'tratten.issues.views.done', name="issue-creation-done"),

    # Login
    (_(r'^login/'), include('tratten.login.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # Logout
    url(_(r'^logout/$'),
        'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name="logout"),

    # Error report
    url(_(r'^error-report/$'),
        'tratten.errorreports.views.report_error',
        name="errorreport"),

    # Internationalization
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(_(r'^language/$'),
        'tratten.preferences.views.select_language',
        name="select-language"),

    # Ping (for monit testing)
    url(_(r'^ping/$'), 'tratten.common.views.ping', name="ping"),

    # Preferences
    (_(r'^preferences/'), include('tratten.preferences.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^(?P<path>favicon\.ico)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

# Switch back to the language of choice
translation.activate(language_saved)
