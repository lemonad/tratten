#
# This backend populates a list with issues fetched from Mantis. Use the
# permalink feature in Mantis to generate a report filtered on items
# that should be included.
#
# Configure which columns in the report correspond to the fields that
# are shown in the list (id, project, assigned to, date submitted,
# summary and status)
#
# The issues can be further filtered by the user via a drop-down control.
#
# TODO: Add caching?
#

#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from datetime import datetime
import re
import simplejson
import sys
import time
from urllib import urlencode
import urllib2

from django.conf import settings
from django.http import ( HttpResponse, HttpResponseNotFound, Http404,
                          HttpResponseRedirect )
from django.utils.translation import ugettext, ugettext_lazy as _

from tratten.categories.models import Category

def fetch_issues(project_filter=None):
    """
    Fetch open issues from Mantis.
    """
    freebusy = {}

    now = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    url = settings.MANTIS_ISSUE_LIST_BACKEND_REPORT_URL

    # Expect local example file path if not an HTTP-based URL
    if re.match('^http', url):
        try:
            auth_handler = urllib2.HTTPBasicAuthHandler()
            cookie_handler = urllib2.HTTPCookieProcessor()
            redirection_handler = urllib2.HTTPRedirectHandler()

            opener = urllib2.build_opener(auth_handler,
                                          cookie_handler,
                                          redirection_handler)

            urllib2.install_opener(opener)
            if settings.MANTIS_USERNAME and settings.MANTIS_PASSWORD:
                login_parameters = {'username': settings.MANTIS_USERNAME,
                                    'password': settings.MANTIS_PASSWORD}
                data = urlencode(login_parameters)
                report_url_data = urlencode({'return': settings.MANTIS_ISSUE_LIST_BACKEND_REPORT_URL})
                login_url = settings.MANTIS_ISSUE_LIST_BACKEND_LOGIN_URL + \
                                "?" + report_url_data
                req = urllib2.Request(login_url, data)
            else:
                login_url = settings.MANTIS_ISSUE_LIST_BACKEND_LOGIN_URL
                req = urllib2.Request(login_url)

            r = urllib2.urlopen(req)
        except urllib2.HTTPError:
            raise Http404(ugettext("Could not fetch issue list from Mantis."))
    else:
        # File-based for testing
        r = open(settings.MANTIS_ISSUE_LIST_BACKEND_REPORT_URL)

    csvreader = csv.reader(r, delimiter=',', quotechar='"')

    # Observe that column numbers in settings are 1-based
    id_name = settings.MANTIS_ISSUE_LIST_BACKEND_ID_NAME
    id_col = settings.MANTIS_ISSUE_LIST_BACKEND_ID_COL - 1
    project_name = settings.MANTIS_ISSUE_LIST_BACKEND_PROJECT_NAME
    project_col = settings.MANTIS_ISSUE_LIST_BACKEND_PROJECT_COL - 1
    assigned_to_name = settings.MANTIS_ISSUE_LIST_BACKEND_ASSIGNED_TO_NAME
    assigned_to_col = settings.MANTIS_ISSUE_LIST_BACKEND_ASSIGNED_TO_COL - 1
    date_submitted_name = settings.MANTIS_ISSUE_LIST_BACKEND_DATE_SUBMITTED_NAME
    date_submitted_col = settings.MANTIS_ISSUE_LIST_BACKEND_DATE_SUBMITTED_COL - 1
    summary_name = settings.MANTIS_ISSUE_LIST_BACKEND_SUMMARY_NAME
    summary_col = settings.MANTIS_ISSUE_LIST_BACKEND_SUMMARY_COL - 1
    status_name = settings.MANTIS_ISSUE_LIST_BACKEND_STATUS_NAME
    status_col = settings.MANTIS_ISSUE_LIST_BACKEND_STATUS_COL - 1

    first_row = csvreader.next()
    if first_row[id_col] != id_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (ID)."))
    if first_row[project_col] != project_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (PROJECT)."))
    if first_row[assigned_to_col] != assigned_to_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (ASSIGNED_TO)."))
    if first_row[date_submitted_col] != date_submitted_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (DATE_SUBMITTED)."))
    if first_row[summary_col] != summary_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (SUMMARY)."))
    if first_row[status_col] != status_name:
        raise Http404(ugettext("Mantis issue list in unexpected format (STATUS)."))

    # Fetch all categories for filtering
    categories = Category.objects.values_list("name", flat=True)
    if project_filter:
        if project_filter not in categories:
            raise Http404(ugettext("Project filter not in list of known categories."))
        else:
            categories = [project_filter]

    issue_list = []
    for row in csvreader:
        if not project_filter or row[project_col] in categories:
            # Replace hyphens with is non breaking spaces
            project_value = re.sub('-', '&#8209;', row[project_col])
            date_submitted_value = re.sub('-', '&#8209;', row[date_submitted_col])
            shortrow = [int(row[id_col]),
                        project_value,
                        row[assigned_to_col],
                        date_submitted_value,
                        row[summary_col],
                        row[status_col]]
            issue_list.append(shortrow)

    issue_list.sort(key=lambda x:datetime.strptime(x[3], "%Y&#8209;%m&#8209;%d").date(),
                    reverse=True)
    return(issue_list)
