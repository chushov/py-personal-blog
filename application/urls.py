from django.contrib import admin
from django.urls import include
from django.urls import path
from main.views import Homepage


urlpatterns = [
    path("", Homepage.as_view()),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
]