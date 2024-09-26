from django.db import models
import uuid


class DeviceManager(models.Manager):
    def create_device(self, id, name, description, type, fields):
        device = self.create(id=id, name=name, description=description, type=type)
        for field in fields:
            DeviceField.objects.create(
                device=device,
                name=field["name"],
                type=field["type"],
                value=field["value"],
            )
        return device

    def update_device(self, device, name, description, type, fields):
        device.name = name
        device.description = description
        device.type = type
        device.save()
        device.fields.all().delete()
        for field in fields:
            DeviceField.objects.create(
                device=device,
                name=field["name"],
                type=field["type"],
                value=field["value"],
            )
        return device


class Device(models.Model):
    objects = DeviceManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class DeviceField(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="fields")
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ["device", "name", "value"]


class DeviceDataManager(models.Manager):
    def create_device_data(self, device_id, field, value):
        device = Device.objects.get(id=device_id)
        field_id = DeviceField.objects.get(device=device, value=field)
        return self.create(device=device, field=field_id, value=value)


class DeviceData(models.Model):
    objects = DeviceDataManager()

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.ForeignKey(DeviceField, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
