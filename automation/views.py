from rest_framework import permissions, viewsets

from .serializers import AutomationSerializer
from .models import Automation


class AutomationViewSet(viewsets.ModelViewSet):
    queryset = Automation.objects.all().order_by("created_at")
    serializer_class = AutomationSerializer
    permission_classes = [permissions.IsAuthenticated]
