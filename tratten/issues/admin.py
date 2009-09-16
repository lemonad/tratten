#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Issue


class IssueAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Reporter'),
            {'fields': ('reporter_name', 'reporter_email', 'reporter_phone')}),
        (_('Category'),
            {'fields': ('category',)}),
        (_('Issue'),
            {'fields': ('summary', 'description', 'urgent')}),
        (_('Due date (optional)'),
            {'fields': ('due_date',)}),
    )
    list_display = ('category', 'reporter_name', 'summary', 'description',
                    'urgent', 'created_at', 'changed_at')
    search_fields = ['summary', 'description']
    filter_list = ['category', 'urgent']

admin.site.register(Issue, IssueAdmin)
