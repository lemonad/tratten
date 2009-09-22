#
# This email backend sends out specially formatted XML messages
# to be picked up by a Mantis plugin that adds corresponding Mantis
# issues.
#
# The idea was to provide a very low-threshold bridge to support
# both this specific frontend for end-users and the creation of
# Mantis issues from administrative scripts (e.g. cron jobs for backups.
# build servers, etc.)
#
#
# TODO: Add DTD
# TODO: Validate XML
#

#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, loader, Template

from tratten.categories.models import Category
from tratten.issues.models import Issue

def on_new_issue_send_mail(issue_id):
    # TODO mark as sent in issues model
    i = Issue.objects.get(id=issue_id)

    t = Template("""<tratten>
    <reporter_name><![CDATA[{{ name }}]]></reporter_name>
    <reporter_email><![CDATA[{{ email }}]]></reporter_email>{% if phone %}
    <reporter_phone><![CDATA[{{ phone }}]]></reporter_phone>{% endif %}
    <entity><![CDATA[{{ entity }}]]></entity>
    <issue_type>Incident</issue_type>
    <urgent>{{ urgent }}</urgent>
    <summary><![CDATA[{{ summary }}]]></summary>
    <description><![CDATA[{{ description }}]]></description>{% if due_date %}
    <reporter_due_date>{{ due_date }}</reporter_due_date>{% endif %}
</tratten>""")
    c = Context({'name': i.reporter_name,
                 'email': i.reporter_email,
                 'phone': i.reporter_phone,
                 'entity': i.category.name,
                 'urgent': "Ja" if i.urgent else "Nej",
                 'summary': i.summary,
                 'description': i.description,
                 'due_date': i.due_date})
    xml = t.render(c)

    send_mail(
        '[Tratten]',
        xml,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_BACKEND_SEND_NEW_ISSUES_TO],
        fail_silently=False)
