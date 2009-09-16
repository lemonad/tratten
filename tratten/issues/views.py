#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import simplejson
import time

from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext, ugettext_lazy as _
from django.template import RequestContext, loader

from models import Issue
from tratten.flatcontent.models import get_flatcontent
from tratten.categories.models import Category

#
# Forms
#


class IssueForm(forms.ModelForm):
    """Form for adding issues."""

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['reporter_name'] = forms.CharField(
                required=True,
                widget=forms.TextInput(attrs={'class': 'span-3'}))
        self.fields['reporter_email'] = forms.CharField(
                required=True,
                widget=forms.TextInput(attrs={'class': 'span-4'}))
        self.fields['reporter_phone'] = forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={'class': 'span-3'}))
        self.fields['category'] = forms.ModelChoiceField(
                required=True,
                queryset=Category.objects.all(),
                empty_label="")
        self.fields['urgent'] = forms.TypedChoiceField(
                coerce=lambda x: bool(int(x)),
                choices=((0, 'Nej'), (1, 'Ja')),
                widget=forms.RadioSelect)
        self.fields['summary'] = forms.CharField(
                required=True,
                widget=forms.TextInput(attrs={'class': 'span-10'}))
        self.fields['description'] = forms.CharField(
                required=False,
                widget=forms.Textarea(attrs={'class': 'span-10'}))
        self.fields['due_date'] = forms.DateField(
                required=False,
                widget=forms.DateInput(attrs={'class': 'span-2',
                                              'id': 'due-date'}))

    class Meta:
      model = Issue
      fields = ('category',
                'summary',
                'description',
                'urgent',
                'due_date',
                'reporter_name',
                'reporter_email',
                'reporter_phone')


#
# Views
#


def index(request):
    """Startpage."""

    description = get_flatcontent('index-text')
    contact_info = get_flatcontent('index-contact-information')

    t = loader.get_template('index.html')
    c = RequestContext(request,
                       {'description': description,
                        'contact_info': contact_info})
    return HttpResponse(t.render(c))

def create(request):
    """Create issue."""

    category_name = get_flatcontent('category-name')
    categories = Category.objects.all()

    if request.method == 'POST':
        issue_form = IssueForm(request.POST, Issue)
        if not issue_form.is_valid():
            request.flash['error'] = ugettext("One or more fields were "
                                              "not properly filled in.")
        else:
            category = issue_form.cleaned_data['category']
            summary = issue_form.cleaned_data['summary']
            description = issue_form.cleaned_data['description']
            urgent = issue_form.cleaned_data['urgent']
            due_date = issue_form.cleaned_data['due_date']
            reporter_name = issue_form.cleaned_data['reporter_name']
            reporter_email = issue_form.cleaned_data['reporter_email']
            reporter_phone = issue_form.cleaned_data['reporter_phone']

            issue_form.save()

            request.flash['success'] = ugettext("New issue "
                                                "successfully created.")
            # Redirect after POST
            return HttpResponseRedirect(reverse('issue-creation-done'))
    else:
        # Initialize form
        issue_form_defaults = \
                        {'category': '',
                         'summary': '',
                         'description': '',
                         'urgent': 0,
                         'due_date': '',}
        issue_form = IssueForm(issue_form_defaults)

    t = loader.get_template('create.html')
    c = RequestContext(request,
                       {'categories': categories,
                        'category_name': category_name,
                        'form': issue_form})
    return HttpResponse(t.render(c))

def done(request):
    """Issue creation done."""
    
    description = get_flatcontent('issue-creation-done-text')

    t = loader.get_template('done.html')
    c = RequestContext(request,
                       {'description': description})
    return HttpResponse(t.render(c))

def list(request):
    """List issues."""

    category_name = get_flatcontent('category-name')
    categories = Category.objects.all()

    t = loader.get_template('list.html')
    c = RequestContext(request,
                       {'categories': categories,
                        'category_name': category_name})
    return HttpResponse(t.render(c))
