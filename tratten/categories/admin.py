#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Category


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Name'),
            {'fields': ('name',)}),
    )
    list_display = ('name', 'created_at', 'changed_at')
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
