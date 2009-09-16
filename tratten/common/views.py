from django.http import HttpResponse
from django.utils.translation import ugettext, ugettext_lazy as _


def ping(request):
    """
    Just output anything in order for monit or similar service monitoring to
    know that "all is well".

    """
    return HttpResponse("OK!")
