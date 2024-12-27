# Create your views here.
from django.http import HttpResponseRedirect


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        "email_confirm_redirect"
    )
