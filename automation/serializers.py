from rest_framework import serializers

from . import models


class ConditionSerializer(serializers.ModelSerializer):
    field = serializers.CharField(source="field.value")

    class Meta:
        model = models.Condition
        fields = ["device", "field", "value", "operator"]


class ActionSerializer(serializers.ModelSerializer):
    field = serializers.CharField(source="field.name")

    class Meta:
        model = models.Action
        fields = ["device", "field"]


class AutomationSerializer(serializers.ModelSerializer):
    conditions = ConditionSerializer(many=True)
    actions = ActionSerializer(many=True)

    class Meta:
        model = models.Automation
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
            "type",
            "conditions",
            "actions",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        return models.Automation.objects.create_automation(**validated_data)

    def update(self, instance, validated_data):
        instance = models.Automation.objects.update_automation(
            instance, **validated_data
        )
        return instance
