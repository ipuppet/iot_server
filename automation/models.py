from django.apps import apps
from django.db import models


Device = apps.get_model("device", "Device")
DeviceField = apps.get_model("device", "DeviceField")


class AutomationManager(models.Manager):
    def create_automation(self, name, description, type, conditions, actions):
        automation = self.create(name=name, description=description, type=type)
        for condition in conditions:
            Condition.objects.create(
                automation=automation,
                device=condition["device"],
                field=condition["field"],
                value=condition["value"],
                operator=condition["operator"],
            )
        for action in actions:
            Action.objects.create(
                automation=automation,
                device=action["device"],
                field=action["field"],
            )
        return automation

    def update_automation(
        self, automation, name, description, type, conditions, actions
    ):
        automation.name = name
        automation.description = description
        automation.type = type
        automation.save()
        automation.conditions.all().delete()
        automation.actions.all().delete()
        for condition in conditions:
            Condition.objects.create(
                automation=automation,
                device=condition["device"],
                field=condition["field"],
                value=condition["value"],
                operator=condition["operator"],
            )
        for action in actions:
            Action.objects.create(
                automation=automation,
                device=action["device"],
                field=action["field"],
            )
        return automation


class Automation(models.Model):
    objects = AutomationManager()

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10)  # and, or
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def conditions(self):
        return self.condition_set.all()

    @property
    def actions(self):
        return self.action_set.all()


class Condition(models.Model):
    automation = models.ForeignKey(
        Automation, on_delete=models.CASCADE, related_name="conditions"
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.ForeignKey(DeviceField, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    operator = models.CharField(max_length=10)


class Action(models.Model):
    automation = models.ForeignKey(
        Automation, on_delete=models.CASCADE, related_name="actions"
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.ForeignKey(DeviceField, on_delete=models.CASCADE)
