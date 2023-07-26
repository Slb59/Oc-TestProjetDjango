"""
URL configuration for library project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("project.account.urls")),
    path("", include("project.library.urls")),
]
