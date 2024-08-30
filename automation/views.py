from rest_framework import permissions, viewsets

from .serializers import AutomationSerializer, ConditionSerializer, ActionSerializer, AutomationConditionSerializer, AutomationActionSerializer
from .models import Automation, Condition, Action, AutomationCondition, AutomationAction


class AutomationViewSet(viewsets.ModelViewSet):
    queryset = Automation.objects.all().order_by("created_at")
    serializer_class = AutomationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AutomationConditionViewSet(viewsets.ModelViewSet):
    queryset = AutomationCondition.objects.all()
    serializer_class = AutomationConditionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AutomationActionViewSet(viewsets.ModelViewSet):
    queryset = AutomationAction.objects.all()
    serializer_class = AutomationActionSerializer
    permission_classes = [permissions.IsAuthenticated]
