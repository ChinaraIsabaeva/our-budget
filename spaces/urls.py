from django.urls import path
from django.contrib import admin

from spaces.views import (
    SpaceCreateView,
    SpaceUpdateView,
    SpaceListView,
    SpaceDeleteView
)


admin.autodiscover()

app_name = 'spaces'

urlpatterns = [
    path(
        'all/',
        SpaceListView.as_view(),
        name='spaces_all'
    ),
    path(
        '<int:pk>/update/',
        SpaceUpdateView.as_view(),
        name='space_update'
    ),
    path(
        'create/',
        SpaceCreateView.as_view(),
        name='space_create'
    ),
    path(
        '<int:pk>/delete/',
        SpaceDeleteView.as_view(),
        name='space_delete'
    )
]
