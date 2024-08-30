from rest_framework import serializers

from . import models


class AutomationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Automation
        fields = ["name", "description", "created_at", "updated_at", "type"]


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Condition
        fields = ["name", "description", "trigger", "value", "operator"]


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Action
        fields = ["name", "description", "action", "target"]


class AutomationConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AutomationCondition
        fields = ["automation", "condition"]


class AutomationActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AutomationAction
        fields = ["automation", "action"]
