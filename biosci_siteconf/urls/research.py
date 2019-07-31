from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from person_tags.models import PersonTag, TagGroup
from person_tags.views import person_tag_create, person_tagged_entry_update

urlpatterns = [
    url(
        r"^$",
        ListView.as_view(queryset=TagGroup.objects.active()),
        name="persontag-taggroup-list",
    ),
    url(
        r"^by-person/$",
        ListView.as_view(
            queryset=TagGroup.objects.active(),
            # queryset=PersonTag.objects.person_list(),
            template_name="person_tags/person_list.html",
        ),
        name="persontag-person-list",
    ),
    url(
        r"^interests/$",
        ListView.as_view(
            queryset=PersonTag.objects.tag_list(),
            template_name="person_tags/tag_list.html",
            context_object_name="tag_list",
        ),
        name="persontag-tag-list",
    ),
    url(
        r"^interests/(?P<slug>[\w-]+)/$",
        DetailView.as_view(
            queryset=PersonTag.objects.active(),
            template_name="person_tags/tag_detail.html",
            context_object_name="tag",
        ),
        name="persontag-tag-detail",
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        DetailView.as_view(queryset=TagGroup.objects.active()),
        name="persontag-taggroup-detail",
    ),
    url(
        r"^tags/(?P<slug>[\w-]+)/update/$",
        person_tagged_entry_update,
        name="persontag-person-tagged-entry-update",
    ),
    url(
        r"^tags/(?P<slug>[\w-]+)/new-tag/$",
        person_tag_create,
        name="persontag-persontag-create",
    ),
    url(r"^tag/new/$", person_tag_create, name="persontag-persontag-create-general"),
]
