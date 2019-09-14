"""URL Configuration."""
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()


urlpatterns = [  # pylint: disable=C0103
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
