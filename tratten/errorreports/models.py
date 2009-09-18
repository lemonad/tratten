from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class ErrorReportManager(models.Manager):
    pass


class ErrorReport(models.Model):
    """
    A user can write an error report for a URL (defined in a template, not
    by the user). The error report is anonymous but the user is encouraged
    to enter an email address.

    # Create
    >>> e = ErrorReport.objects.create(url='/', reported_by="jonas@example.com",
    ...     report="Test", status=1)
    >>> e.url
    '/'
    >>> e.save()
    >>> e = ErrorReport.objects.get(pk=e.pk)
    >>> e
    <ErrorReport: Test>

    # Delete object
    >>> e.delete()
    """

    STATUS_TYPES = \
        ((1, _('Open')),
         (2, _('More information needed')),
         (3, _('Closed')))

    url = models.CharField(_('relative url'),
                           max_length=255,
                           db_index=True)
    reported_by = models.EmailField(_('reported by'),
                                    max_length=255,
                                    blank=True,
                                    db_index=True)
    report = models.TextField(_('error report'))
    status = models.PositiveIntegerField(_('status'),
                                         db_index=True,
                                         choices=STATUS_TYPES)
    date_created = models.DateTimeField(_('created (date)'),
                                        db_index=True,
                                        auto_now_add=True)
    date_modified = models.DateTimeField(_('modified (date)'),
                                         db_index=True,
                                         auto_now=True)
    objects = ErrorReportManager()

    def __unicode__(self):
        return self.report

    class Meta:
        # FIXME: permissions does not seem to use ugettext
        ordering = ['-date_created']
        verbose_name = _('error report')
        verbose_name_plural = _('error reports')
        permissions = (("receive_email_on_error_reports",
                       ugettext("Receives email when errors are reported")),)
