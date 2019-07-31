"""
url patterns for the site.
"""
import os

## LOAD shout sources
import shouts
from admin_export.actions import SPREADSHEET_EXPORT_ACTIONS
from classes.views import advertised_section_list
from django.conf import settings
from django.conf.urls import handler500, include, url
from django.contrib import admin

# Enable export actions globaly
from django.contrib.admin.sites import site
from django.views.generic import RedirectView, TemplateView
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve as static_serve

# UNregister student app admins
from students.models import (
    RequirementTag,
    SectionRequirement,
    Student,
    Student_Registration,
    iclicker,
)

from ..decorators import secure_required

for action in SPREADSHEET_EXPORT_ACTIONS:
    site.add_action(action, action.__name__)


# setup better error pages
handler403 = "uofm.views.permission_denied"
handler404 = "uofm.views.not_found"
handler500 = "uofm.views.server_error"

# from uofm.forms import UMAuthenticationForm
urlpatterns = []

if os.environ.get("FOS_LOOK", True):
    urlpatterns += [
        url(
            r"^$",
            # TemplateView.as_view(template_name='fos/site_splash.html'),
            RedirectView.as_view(
                url="https://www.sci.umanitoba.ca/biological-sciences/", permanent=False
            ),
            name="home-page",
        ),
        url(r"^events-calendar/", include("shouts.eventscalendar.urls")),
    ]

urlpatterns += [
    # This never gets called in the production site.
    url(
        r"^%s(.*)$" % settings.MEDIA_URL[1:],
        static_serve,
        kwargs={"document_root": settings.MEDIA_ROOT},
    ),
    # example redirect:
    # url(r'^cma/', RedirectView.as_view(url='/administration/')),
    # url includes:
    url(r"^cma/export/", include("admin_export.urls")),
    url(r"^cma/", admin.site.urls),
    url(r"^classes/$", advertised_section_list, name="biosci-classes-index"),
    url(r"^classes/", include("classes.urls")),
    url(r"^seminars/", include("seminars.urls")),
    url(
        r"^directory/", include("biosci_siteconf.urls.dept_directory")
    ),  # include('directory.urls')),
    url(r"^grad-students/", include("graduate_students.urls")),
    url(r"^research/publications/", include("publications.urls")),
    url(r"^research/", include("biosci_siteconf.urls.research")),
    url(r"^people/", include("person_pages.urls")),
    url(r"^notices/", include("shouts.urls")),
    url(r"^positions/", include("jobpost.urls")),
    url(r"^room-schedules/", include("swingtime.urls")),
    url(r"^shares/", include("fileshare.urls")),
    url(r"^profile/", include("people.urls")),
    url(r"^jsi18n/$", JavaScriptCatalog.as_view(), name="site-jsi18n"),
    url(r"^", include("uofm.urls")),
]

if settings.USE_HAYSTACK:
    urlpatterns.append(url(r"^search/", include("haystack.urls")))

if settings.DEBUG and getattr(settings, "USE_DEBUG_TOOLBAR", False):
    import debug_toolbar

    urlpatterns += [url(r"^__debug__/", include(debug_toolbar.urls))]

# Unitpages must be last when used at the top level,
#   due to it's internal resolution mechanism
urlpatterns.append(url(r"^", include("unitpages.urls")))

shouts.autodiscover()


admin.site.unregister(Student)
admin.site.unregister(iclicker)
admin.site.unregister(Student_Registration)
admin.site.unregister(SectionRequirement)
