#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models import (Manager, Model, BooleanField, CharField,
                              DateField, DateTimeField, EmailField,
                              FloatField, ForeignKey, ManyToManyField,
                              TextField)
from django.utils.translation import ugettext_lazy as _

from tratten.categories.models import Category


class IssueManager(Manager):
    pass


class Issue(Model):
    """A (service desk) issue.

    >>> c = Category(name="Build server")
    >>> c.save()
    >>> i = Issue(category=c,
    ...           urgent=True,
    ...           summary="HTTP Error 500 on rebuild",
    ...           reporter_name="Jonas Nockert",
    ...           reporter_email="jonasnockert@gmail.com")
    >>> i.save()

    """

    category = ForeignKey(Category,
                          verbose_name=_("Category"),
                          db_index=True)
    summary = CharField(_("Summary"),
                        db_index=True,
                        max_length=128)
    description = TextField(_("Description"),
                            blank=True)
    urgent = BooleanField(_("Urgent?"),
                          db_index=True,
                          default=False)
    due_date = DateField(_("Due date"),
                         null=True,
                         blank=True,
                         db_index=True)
    reporter_name = CharField(_("Reporter name"),
                              db_index=True,
                              max_length=48)
    reporter_email = EmailField(_("Reporter email"),
                                db_index=True,
                                max_length=64)
    reporter_phone = CharField(_("Reporter phone number"),
                               null=True,
                               max_length=32)
    created_at = DateTimeField(_("Created"),
                               db_index=True,
                               auto_now_add=True)
    changed_at = DateTimeField(_("Changed"),
                               db_index=True,
                               auto_now=True)
    objects = IssueManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("issue")
        verbose_name_plural = _("issues")

    def __unicode__(self):
        return self.summary
