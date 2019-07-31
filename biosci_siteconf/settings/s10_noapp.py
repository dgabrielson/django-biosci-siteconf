################################################
# Non-Application settings.
################################################

from .auth import *

################################################

# Cookie settings

SESSION_COOKIE_SECURE = False  # must be running over SSL for this to be True.
if DEBUG:
    SESSION_COOKIE_SECURE = False  # Otherwise runserver will not do cookies (& no auth)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 24 * 60 * 60  # 1 day, in seconds

################################################

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

################################################

# Login / Logout urls.

# django-uofm uses these settings
#   do not use reverse_lazy() for LOGIN/OUT_URL.
LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"

################################################

# Mail settings:

SERVER_EMAIL = "biosciadmin@biosci.umanitoba.ca"
DEFAULT_FROM_EMAIL = "no-reply@biosci.umanitoba.ca"

################################################

FACE_DETECT_CONFIG = {
    "crop:resize": (90, 90),
    "highlight:resize": None,
    "minimum_size_factor": 0.02,  # must be between 0 and 1
}

################################################
