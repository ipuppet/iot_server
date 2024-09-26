from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_device(sender, **kwargs):
    from .models import Device

    try:
        if Device.objects.exists():
            return
        Device.objects.create_device(
            id="A20D1CBE-78A3-41AF-9A61-D5243914A0E6",
            name="Temperature & Humidity Sensor",
            description="A temperature and humidity sensor",
            type="condition",
            fields=[
                {"name": "Temperature", "value": "temperature"},
                {"name": "Humidity", "value": "humidity"},
            ],
        )
        Device.objects.create_device(
            id="B131E7F7-695E-442B-851F-4A8EE00A34FF",
            name="Dust Sensor",
            description="A dust sensor",
            type="condition",
            fields=[
                {"name": "Dust", "value": "dust"},
            ],
        )
    except Exception as e:
        print("Init device failed:", e)
        exit(1)


class DeviceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "device"

    def ready(self):
        post_migrate.connect(init_device, sender=self)
