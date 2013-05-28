from django.http import HttpResponseRedirect
from django.conf import settings

def not_logged_in_required(func):
    """
    Decorator that ensures that user is not logged in.
    """
    def wrapper(request, *args, **kw):
        if request.user.is_authenticated():
            # the user is logged in
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            return func(request, *args, **kw)
    return wrapper
