from django.urls import path

from . import api

urlpatterns = [
    path("groups/", api.Groups.as_view(),),
#    path("publications/", api.Publications.as_view(),),
]
