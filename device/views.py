from rest_framework import permissions, viewsets, mixins

from .serializers import DeviceSerializer, DeviceDataSerializer
from .models import Device, DeviceData


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by("created_at")
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceDataViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = DeviceDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs["id"]
        return DeviceData.objects.filter(device=device_id).order_by("timestamp")

    def perform_create(self, serializer):
        device_id = self.kwargs["id"]
        serializer.save(device_id=device_id)
