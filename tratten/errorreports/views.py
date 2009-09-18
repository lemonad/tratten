from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.mail import send_mail, mail_admins
from django.db.models import Q
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect)
from django.shortcuts import (get_object_or_404, get_list_or_404,
                              render_to_response)
from django.template import RequestContext, loader
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext, ugettext_lazy as _

from models import ErrorReport


#
# Forms
#


class ErrorReportForm(forms.Form):
    """
    Form for submitting error reports.

    """
    report = forms.CharField(
        label="",
        widget=forms.Textarea(attrs = {'id': 'set-focus',
                                       'rows': '10',
                                       'cols': '60'}),
        help_text=_("Describe the error(s) here. If possible, also mention "
                  "what you think the correct information should be."))
    reported_by = forms.EmailField(label=_("Your email address"))


#
#
#

def report_error(request):
    """
    Form for submitting error reports. Also handles form submittal.

    """
    if not request.GET or 'url' not in request.GET:
        raise Http404(ugettext("Query string missing."))
    url = request.GET['url']

    if request.method == 'POST':
        # The error report form has been submitted
        form = ErrorReportForm(request.POST, auto_id=False)
        if form.is_valid():
            report = form.cleaned_data['report']
            email = form.cleaned_data['reported_by']
            r = ErrorReport(url=url, report=report,
                            reported_by=email, status=1)
            r.save()

            # Get name of person, if available
            try:
                u = User.objects.get(email=email)
                reported_by = "%s (%s)" % (u.get_full_name(), email)
            except User.DoesNotExist:
                reported_by = email

            # Find everyone with the 'permissions' to receive emails on
            # error reports
            content_type = ContentType.objects.get_for_model(ErrorReport)
            users = User.objects \
                      .filter(Q(user_permissions__codename=
                                'receive_email_on_error_reports') &
                              Q(user_permissions__content_type=content_type)) \
                      .exclude(is_active=False)
            recipients = []
            for u in users:
                recipients.append(u.email)

            email_subject = ugettext("error report from %(reported_by)s") % {
                                          'reported_by': reported_by}
            current_site = Site.objects.get_current()
            email_body = ugettext("URL: http://%(domain)s%(path)s\n"
                                  "Reported by: %(reported_by)s\n\n"
                                  "%(report)s") % {
                                      'domain': current_site.domain,
                                      'path': url,
                                      'reported_by': reported_by,
                                      'report': report}

            # If no users are found, email error message to all
            # administrator(s)
            if len(recipients) <= 0:
                email_body += ugettext(
                    "\n\n"
                    "----------\n"
                    "This email has been automatically sent to all "
                    "administrators listed in 'settings.ADMINS'.\nNote that "
                    "you can use the permission "
                    "'receive_email_on_error_reports' to select who will "
                    "receive error reports.")
                mail_admins(email_subject, email_body, fail_silently=True)
                request.flash.now['success'] = ugettext(
                                        "Your error report was "
                                        "successfully created and emailed to "
                                        "all administrators.")
            else:
                email_subject = smart_unicode(
                                    settings.EMAIL_SUBJECT_PREFIX) + \
                                    email_subject
                send_mail(email_subject, email_body,
                          settings.DEFAULT_FROM_EMAIL, recipients,
                          fail_silently=True)
                request.flash.now['success'] = ugettext(
                                        "Your error report was "
                                        "successfully created and emailed to "
                                        "assigned staff members.")

            # Form has been posted, pre-fill new form
            default_data = {'report': "", 'reported_by': email}
            form = ErrorReportForm(default_data, auto_id=False)
        else:
            request.flash.now['error_form'] = ugettext("Not all fields were "
                                                        "properly filled in.")
    else:
        try:
            email = request.user.email
        except AttributeError:
            email = None

        # pre-fill form
        default_data = {'report': "", 'reported_by': email}
        form = ErrorReportForm(default_data, auto_id=False)

    error_reports = ErrorReport.objects.filter(url=url)

    return render_to_response('report-error.html', {
            'form': form,
            'url': url,
            'error_reports': error_reports,
        },
        context_instance=RequestContext(request))
