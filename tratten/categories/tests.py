"""
Tests for categories.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlquote
from django.utils.translation import ugettext

from models import Category


class CategoryModelTests(TestCase):
    fixtures = ['categories.json']

    def setUp(self):
        pass

    def test_category_creation(self):
        c = Category(name="Production servers")
        c.save()
        cid = c.id
        c = Category.objects.get(id=cid)
        self.failUnlessEqual(c.name, "Production servers")

    def test_category_deletion(self):
        c = Category.objects.all()[0]
        cid = c.id
        c.delete()
        self.assertRaises(ObjectDoesNotExist, Category.objects.get, id=cid)
