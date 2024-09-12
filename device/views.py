from rest_framework import permissions, viewsets
from rest_framework import viewsets, permissions

from .serializers import DeviceSerializer, DeviceDataSerializer
from .models import Device, DeviceData


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by("created_at")
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceDataViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        if device_id:
            return DeviceData.objects.filter(device=device_id).order_by("timestamp")
        return DeviceData.objects.none()
