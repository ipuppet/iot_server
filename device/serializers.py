from rest_framework import serializers

from . import models


class DeviceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceField
        fields = ["name", "value"]


class DeviceDataSerializer(serializers.ModelSerializer):
    field = serializers.CharField()

    class Meta:
        model = models.DeviceData
        fields = ["field", "value", "timestamp"]
        read_only_fields = ["timestamp"]

    def create(self, validated_data):
        return models.DeviceData.objects.create_device_data(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["field"] = instance.field.value
        return data


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
