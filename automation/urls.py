from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"automation", views.AutomationViewSet)
router.register(r"automation_condition", views.AutomationConditionViewSet)
router.register(r"automation_action", views.AutomationActionViewSet)

urlpatterns = []
urlpatterns += router.urls
