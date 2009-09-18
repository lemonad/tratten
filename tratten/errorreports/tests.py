"""
Tests for error reports.

"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlquote
from django.utils.translation import ugettext

from models import ErrorReport


class ErrorReportTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        pass

    def test_expect_404_when_url_not_defined(self):
        # Expect 404 when url not defined
        response = self.client.get(reverse('errorreport'))
        self.failUnlessEqual(response.status_code, 404)

    def test_expect_200_when_url_defined(self):
        response = self.client.get(reverse('errorreport'), {"url": "/"})
        self.failUnlessEqual(response.status_code, 200)

    def test_error_report_email(self):
        # Send error report and verify that email has been sent out
        self.assertTrue(len(mail.outbox) == 0)
        # ...with valid email...
        user = User.objects.all()[0]
        # Django 1.0.2+ required to combine GET and POST in test framework!
        url = reverse('errorreport') + "?url=/"
        response = self.client.post(url,
                                    {"report": "Test of error report.",
                                     "reported_by": user.email})
        self.failUnlessEqual(response.status_code, 200)
        self.assertTrue(len(mail.outbox) > 0)

    def test_error_report_invalid_email(self):
        # Django 1.0.2+ required to combine GET and POST in test framework!
        url = reverse('errorreport') + "?url=/"
        response = self.client.post(url,
                                    {"report": "Test of error report.",
                                     "reported_by": "testuser"})
        self.failUnlessEqual(response.status_code, 200)
