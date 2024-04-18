from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # admin site
    path("__debug__/", include("debug_toolbar.urls")),  # debug toolbar
    path("", include("jobs.urls")),  # send users to base app urls
    path("login/", include("login.urls")),  # send users to login app urls
]
