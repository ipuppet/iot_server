from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"devices", views.DeviceViewSet)
router.register(
    r"devices/(?P<id>[0-9a-fA-F-]+)/data", views.DeviceDataViewSet, "device-data"
)

urlpatterns = router.urls
