# Django settings for biosci project.
# See: https://docs.djangoproject.com/en/dev/ref/settings/ for information.

from .load_json_conf import json_conf
from .post_local import finalize_settings
from .s10_noapp import *
from .s50_logging import LOGGING
from .templates import TEMPLATES

del DEFAULT_CONTENT_TYPE  # remove in Django 3.0

# a dev default database
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/dev/null/data.db"}
}
"""
$ ./manage.py shell
from django.utils.crypto import get_random_string ;\
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)" ;\
print "SECRET_KEY = {0!r}".format(get_random_string(50, chars))
"""
SECRET_KEY = "this-is-my-secret-key_(actually-set-in-local_settings.py)"

WSGI_APPLICATION = "biosci_siteconf.wsgi.application"

ROOT_URLCONF = "biosci_siteconf.urls"
TIME_ZONE = "America/Winnipeg"
USE_TZ = True
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = False
USE_L10N = True

MEDIA_ROOT = "/dev/null/media"
MEDIA_URL = "/media/"

STATIC_ROOT = "/dev/null/static"
STATIC_URL = "/static/"

HTTPS_ENABLED = not DEBUG  # for the secure_required decorator

FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644
ADMIN_MEDIA_PREFIX = "/cma/static/"

#########################################################

locals().update(json_conf())
locals().update(finalize_settings(locals()))

#########################################################
