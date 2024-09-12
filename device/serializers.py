from rest_framework import serializers

from . import models


class DeviceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceField
        fields = ["name", "type", "target"]


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceData
        fields = ["device", "name", "value", "timestamp"]


class DeviceSerializer(serializers.ModelSerializer):
    fields = DeviceFieldSerializer(many=True)

    class Meta:
        model = models.Device
        fields = ["id", "name", "description", "type", "fields"]

    def create(self, validated_data):
        return models.Device.objects.create_device(**validated_data)

    def update(self, instance, validated_data):
        instance = models.Device.objects.update_device(instance, **validated_data)
        return instance
