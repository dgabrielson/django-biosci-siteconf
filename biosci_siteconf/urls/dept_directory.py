from directory.models import DirectoryEntry, EntryType
from directory.views import DirectoryEntryUpdateView, by_person_detail
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

urlpatterns = [
    url(
        r"^$",
        ListView.as_view(
            queryset=DirectoryEntry.objects.active(),
            template_name="directory/visual_1col/directoryentry_list.html",
        ),
        name="directory-entry-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        DetailView.as_view(
            queryset=EntryType.objects.active(),
            template_name="directory/visual_1col/entrytype_detail.html",
        ),
        name="directory-entrytype-detail",
    ),
    url(
        r"^entry/(?P<pk>[\d]+)/update/$",
        login_required(
            DirectoryEntryUpdateView.as_view(
                template_name="directory/visual_1col/directoryentry_form.html"
            )
        ),
        name="directory-visual-1col-entry-update",
    ),
    url(
        r"^entry/(?P<slug>[\w-]+)/$",
        by_person_detail,
        name="directory-by-person-detail",
    ),
]
