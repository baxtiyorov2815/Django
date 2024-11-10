from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("", include("core.urls")),
]
