from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from log_processor.views import LogEntryViewSet


router_v1 = DefaultRouter()
router_v1.register(r"logs", LogEntryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]
