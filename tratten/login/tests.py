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

class LoginTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        pass

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.failUnlessEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get(reverse('logout'))
        self.failUnlessEqual(response.status_code, 200)

    def test_login_via_post(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'testclient',
                                     'password': 'password'})
        self.assertRedirects(response,
                             reverse('index'),
                             status_code=302,
                             target_status_code=200)
