from rest_framework.routers import DefaultRouter
from django.urls import re_path

from . import views

router = DefaultRouter()
router.register(r"devices", views.DeviceViewSet)
router.register(
    r"devices/(?P<id>[0-9a-fA-F-]+)/data", views.DeviceDataViewSet, "device-data"
)
urlpatterns = [
    re_path(
        r"devices/(?P<id>[0-9a-fA-F-]+)/run",
        views.DeviceRun.as_view(),
        name="device-run",
    ),
]

urlpatterns += router.urls
