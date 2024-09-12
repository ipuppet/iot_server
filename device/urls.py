from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"devices", views.DeviceViewSet)
router.register(r"devices/(?P<id>\d+)/data", views.DeviceDataViewSet, "device-data")

urlpatterns = router.urls
