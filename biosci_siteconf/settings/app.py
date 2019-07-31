################################################

import os

import django
from django.urls import reverse_lazy

from .contacts import *
from .paths import *

################################################
# BioSci template overrides.
if os.environ.get("FOS_LOOK", True):
    INSTALLED_APPS += ("science2018",)

INSTALLED_APPS += ("biosci_templates",)

#################################################

# Additional contrib dependencies for local apps
INSTALLED_APPS += (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.staticfiles",
)

###############################################
# Application: UofM
# Purpose: Provide UofM look and feel, as well as certain uofm specific
#   integration points.

INSTALLED_APPS += ("uofm",)
UNIT_SITE_CONFIG = {
    "long_unit_name": "Department of Biological Sciences",
    "short_unit_name": "Biology",
    "unit_building_addr": "General Office 212B Bio-Sci Bldg., 50 Sifton Road",
    "unit_contact_phone": "204-474-9245",
    "unit_contact_fax": "204-474-7604",
    "unit_contact_email": None,
    "other_site_links": (("Faculty of Science", "http://umanitoba.ca/science"),),
    "unit_course_prefix": "BIOL",
    # just the name:
    "unit_twitter_name": None,
    # full urls (or None):
    "unit_facebook_page": "https://www.facebook.com/pages/Department-of-Biological-Sciences-University-of-Manitoba/1419851884992136",
    "unit_youtube_channel": "https://www.youtube.com/user/BioSciUniMan/",
    "rss_news_feed_url": "http://news.umanitoba.ca/tag/biological-sciences/",
    "event_calendar_url": "https://eventscalendar.umanitoba.ca/site/science/page/quicklinks/?id=d12b6d1d-22eb-4df0-8bf7-d0d4736413fc",
    # Splash images: use dynamic list or single static image?
    # Template is: ``uofm/splash_images.html`` (when ``True``)
    #   or ``uofm/includes/splash/image.html`` (when ``False``)
    "use_splash_image_list": True,
}

################################################
# Application: UnitPages
# Purpose: Core content management system, provides arbitary pages

INSTALLED_APPS += ("unitpages",)

UNITPAGES_CONFIG = {
    # This is the path where site files get uploaded.
    "upload_path": "biol/%Y/%m"
}

################################################
# Application: MarkupHelpers
# Purpose: Provide enhanced widgets for editing reStructuredText

INSTALLED_APPS += ("markuphelpers",)

################################################
# Application: Django LaTeX
# Purpose: Provide templatetags for working with LaTeX / PDF generation

INSTALLED_APPS += ("django_latex",)

################################################
# Application: Swingtime
# Purpose: Room booking / scheduling

SWINGTIME_SETTINGS_MODULE = "swingtime.conf.swingtime_settings"
INSTALLED_APPS += ("swingtime",)

################################################
# Application: Seminars
# Purpose: Announcement and management of seminars

INSTALLED_APPS += ("seminars",)

# seminars settings - note that the ADMINS setting is required.
LOCATION_MODEL_NAME = "places.ClassRoom"
SEMINAR_UPCOMING_WEEKS_IN_ADVANCE = 6
SEMINAR_UPCOMING_MAX_COUNT = 4

SEMINAR_TERMS_IN_GLANCE = 3

################################################
# Application: Classes, Aurora
# Purpose: Course information, Sections, etc.

# The aurora app is only required if loading class info from aurora

INSTALLED_APPS += ("classes", "aurora", "exams", "students")
CLASSES_CONFIG = {
    "default_class_code": "BIOL",
    "advertised_class_codes": ["BIOL"],
    "aurora_fetch_class_codes": ["BIOL"],  # also useful: GRAD
    "api:important_dates_src_url": "http://10.10.26.12/classes/api/important-dates/future/",
}

################################################
# Application: people, places, directory, person_tags
# Purpose: Core Personal Information Management.

INSTALLED_APPS += (
    #    'random_image',  # for unknown faces    # NOTE: currently unused.
    "people",
    "places",
    "directory",
    "person_tags",
)


def get_person_permalink(person):
    """
    provides a pluggable system for mapping person objects
    to a page, used by person.get_absolute_url -- this is either
    'None' (no personal pages) or a tuple ('named-view, arg_map)
    where the arg map is a callable which maps the person object
     into the correct arguments for the view.
    """
    if not person.active:
        return None
    if person.slug is None:
        return None
    from person_pages.models import PersonPage

    try:
        page = PersonPage.objects.get(active=True, person=person)
    except PersonPage.DoesNotExist:
        return None
    return page.get_absolute_url()


PEOPLE_CONFIG = {
    "permalink": get_person_permalink,
    "extra_person_forms": [
        "people.forms.PersonFlagsPersonSubForm",
        "people.forms.EmailAddressPersonSubForm",
        "directory.forms.DirectoryEntryPersonSubForm",
        "person_pages.forms.PersonPagePersonSubForm",
    ],
    "admin_person_default_query": None,
}

##### DIRECTORY SETTINGS #####
PHONENUMBER_DEFAULT_REGION = "CA"

DIRECTORY_CONFIG = {
    # These should remain constant througout your sites lifetime.
    "localflavor": {
        "region": "localflavor.ca.forms.CAProvinceField",
        "postalcode": "localflavor.ca.forms.CAPostalCodeField",
    },
    # provide extra (static) context for all directory views
    # (these can be changed as needed)
    "extra_context": {
        "page1_slugs": [
            "faculty",
            "support-staff",
            "post-docs",
            "sessionals",
            "technicians",
        ],
        "page2_slugs": [],
    },
}

################################################
# Application: Person_pages
# Purpose: Personal pages for individuals, allows for people to edit
#   their own pages.

INSTALLED_APPS += ("face_detect", "person_pages")

################################################
# Application: Graduate_students
# Purpose: Manage graduate student and alumni information

GRADUATE_STUDENT_CONFIG = {"jsi18n_url": reverse_lazy("site-jsi18n")}

INSTALLED_APPS += ("graduate_students",)

################################################
# Application: Shouts
# Purpose: Provide sidebar information.

INSTALLED_APPS += ("shouts",)

if os.environ.get("FOS_LOOK", True):
    INSTALLED_APPS += ("shouts.eventscalendar",)

################################################
# Application: Publications
# Purpose: Provide a unit-wide publication database.

INSTALLED_APPS += ("publications",)
PUBLICATIONS_CONFIG = {
    # The number of publications which show up from
    #   Publication.objects.recent()
    "recent_count": 5,
    # The number of years which show up in the main page
    "recent_years": 3,
}

################################################
# Application: JobPost
# Purpose: Manage Job opportunities.

INSTALLED_APPS += ("jobpost",)

################################################
# Application: Course_Groups
# Purpose: Provide an organizational layer for courses
# (unused)
# INSTALLED_APPS += ('course_groups',)

################################################
# Application: Fileshare
# Purpose: Distribute files only to authorized users

INSTALLED_APPS += ("fileshare",)
FILESHARE_CONFIG = {
    "share_path": "/dev/null/__share",
    "use_sendfile": False,  # sendfile is disabled when DEBUG == True.
}

################################################
# Application: Office_Mgmt
# Purpose: Manage Assets and other paperwork.

INSTALLED_APPS += ("office_mgmt",)

################################################
# Application: Committee
# Purpose: Model and track committee arangements

INSTALLED_APPS += ("committee",)

################################################
# Application: Course Planning
# Purpose: Course scheduling and programs

INSTALLED_APPS += ("course_planning",)

################################################
####
####  The remainder of this file loads 3rd party apps
####
################################################

###############################################
# Application: guardian
# Purpose: per-object permissions

INSTALLED_APPS += ("guardian",)

AUTHENTICATION_BACKENDS += ("guardian.backends.ObjectPermissionBackend",)
ANONYMOUS_USER_ID = -1

###############################################
# django-haystack
# http://haystacksearch.org/

USE_HAYSTACK = True
INSTALLED_APPS += ("haystack",)
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.expanduser("~/whoosh_index"),
        "STORAGE": "file",
        "POST_LIMIT": 128 * 1024 * 1024,
        "INCLUDE_SPELLING": False,
        "BATCH_SIZE": 100,
    }
}

###############################################
