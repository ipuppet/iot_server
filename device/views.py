from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import DeviceSerializer, DeviceDataSerializer
from .models import Device, DeviceData, DeviceField

from automation.automation import AutomationManager


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
        return DeviceData.objects.filter(device=device_id).order_by("-timestamp")

    def perform_create(self, serializer):
        device_id = self.kwargs["id"]
        serializer.save(device_id=device_id)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        am = AutomationManager()
        infrareds = am.check_automations()
        if len(infrareds) > 0:
            response.data["infrareds"] = infrareds
        return response


class DeviceRun(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, id):
        field_name = request.data["field"]
        try:
            field = DeviceField.objects.get(device=id, name=field_name)
            async_to_sync(self.send_signal_to_group)(field.value)
            return Response(status=200)
        except DeviceField.DoesNotExist:
            return Response(status=404)

    async def send_signal_to_group(self, signal):
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            "infrared_control",
            {
                "type": "run_signal",
                "signal": signal,
            },
        )
