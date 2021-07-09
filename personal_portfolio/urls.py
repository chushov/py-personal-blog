from django.contrib import admin
from django.urls import include
from django.urls import path

from django.conf.urls.static import static
from django.conf.urls.static import settings
from main.views import Homepage

urlpatterns = [
    # Homepage path definition.
    path("", Homepage.as_view()),
    # Same as above but using regular expressions (just an example).
    # from django.urls import re_path
    # re_path(r"^$", Homepage.as_view()),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
