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

from tratten.categories.models import Category
from models import Issue


class IssueModelTests(TestCase):
    fixtures = ['categories.json', 'issues.json']

    def setUp(self):
        pass

    def test_issue_creation(self):
        c = Category.objects.all()[0]

        i = Issue(summary="Test",
                  description="Test",
                  reporter_name="User",
                  reporter_email="test@example.com",
                  urgent=True,
                  category=c)
        i.save()
        iid = i.id
        i = Issue.objects.get(id=iid)
        self.failUnlessEqual(i.summary, "Test")

    def test_issue_deletion(self):
        i = Issue.objects.all()[0]
        iid = i.id
        i.delete()
        self.assertRaises(ObjectDoesNotExist, Issue.objects.get, id=iid)

class IssueUnauthorizedTests(TestCase):
    fixtures = ['categories.json', 'issues.json']

    def setUp(self):
        pass

    def test_index_view_unauth(self):
        """Make sure view loads properly."""
        response = self.client.get(reverse('index'))
        self.failUnlessEqual(response.status_code, 200)

    def test_create_issue_view_unauth(self):
        """Make sure view loads properly."""
        response = self.client.get(reverse('create-issue'))
        self.failUnlessEqual(response.status_code, 200)

    def test_list_issues_view_unauth(self):
        """Make sure view loads properly."""
        response = self.client.get(reverse('list-issues'))
        self.failUnlessEqual(response.status_code, 200)

    def test_issue_creation_done_view_unauth(self):
        """Make sure view loads properly."""
        response = self.client.get(reverse('issue-creation-done'))
        self.failUnlessEqual(response.status_code, 200)

    def test_create_issue_via_incomplete_form(self):
        """Make sure create issue view does not accept incomplete forms."""

        c = Category.objects.all()[0]

        # Category missing
        response = self.client.post(reverse('create-issue'),
                                    {'urgent': 1,
                                     'summary': 'Test',
                                     'reporter_name': 'Name',
                                     'reporter_email': 'test@example.com',})
        self.assertFormError(response, 'form', 'category',
                             ugettext("This field is required."))

        # Urgency missing
        response = self.client.post(reverse('create-issue'),
                                    {'category': c.id,
                                     'summary': 'Test',
                                     'reporter_name': 'Name',
                                     'reporter_email': 'test@example.com',})
        self.assertFormError(response, 'form', 'urgent',
                             ugettext("This field is required."))

        # Summary missing
        response = self.client.post(reverse('create-issue'),
                                    {'category': c.id,
                                     'urgent': 0,
                                     'reporter_name': 'Name',
                                     'reporter_email': 'test@example.com',})
        self.assertFormError(response, 'form', 'summary',
                             ugettext("This field is required."))

        # Reporter name missing
        response = self.client.post(reverse('create-issue'),
                                    {'category': c.id,
                                     'urgent': 0,
                                     'summary': 'Test',
                                     'reporter_email': 'test@example.com',})
        self.assertFormError(response, 'form', 'reporter_name',
                             ugettext("This field is required."))

        # Reporter email missing
        response = self.client.post(reverse('create-issue'),
                                    {'category': c.id,
                                     'urgent': 0,
                                     'summary': 'Test',
                                     'reporter_name': 'Name',})
        self.assertFormError(response, 'form', 'reporter_email',
                             ugettext("This field is required."))

    def test_create_issue_via_incomplete_form(self):
        """
        Make sure create issue view accept complete forms.
        
        Note that urgent is submitted as 0/1 but later coerced to False/True.
        """

        c = Category.objects.all()[0]

        response = self.client.post(reverse('create-issue'),
                                    {'category': c.id,
                                     'urgent': 0,
                                     'summary': 'Test',
                                     'reporter_name': 'Name',
                                     'reporter_email': 'test@example.com',})
        self.assertRedirects(response, reverse('issue-creation-done'),
                             status_code=302, target_status_code=200)
