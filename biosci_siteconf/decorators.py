"""
Decorators for this site.
"""
from django.conf import settings
from django.http import HttpResponseRedirect

HTTPS_ENABLED = getattr(settings, "HTTPS_ENABLED", False)

# HTTPS_ENABLED = True should be set in local_settings.py


def secure_required(view_func):
    """
    Decorator makes sure URL is accessed over ssl.
    """

    def _wrapped_view_func(request, *args, **kwargs):
        if not request.is_secure():
            if HTTPS_ENABLED:
                url = request.build_absolute_uri(request.get_full_path())
                ssl_url = url.replace("http://", "https://")
                return HttpResponseRedirect(ssl_url)
        return view_func(request, *args, **kwargs)

    # set a nice doc string
    _wrapped_view_func.__doc__ = ""
    if view_func.__doc__ is not None:
        _wrapped_view_func.__doc__ += view_func.__doc__ + "\n"
    _wrapped_view_func.__doc__ += "[Wrapped by secure_required]"

    return _wrapped_view_func
