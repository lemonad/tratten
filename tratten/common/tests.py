#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from django.core.urlresolvers import reverse
from django.test import TestCase

class MiscTestCase(TestCase):

    def setUp(self):
        pass

    def test_ping(self):
        response = self.client.get(reverse('ping'))
        self.failUnlessEqual(response.status_code, 200)

