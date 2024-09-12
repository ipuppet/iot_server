from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"devices", views.DeviceViewSet)
router.register(r"(?P<device_id>\d+)/data", views.DeviceDataViewSet)

urlpatterns = router.urls
