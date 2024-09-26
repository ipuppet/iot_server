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
                target=field["target"],
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
                target=field["target"],
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
    type = models.CharField(max_length=10)
    target = models.CharField(max_length=100)


class DeviceData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.ForeignKey(DeviceField, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
