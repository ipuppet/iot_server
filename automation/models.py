from typing import Any
from django.db import models


class AutomationManager(models.Manager):
    def create_automation(self, name, description, type, conditions, actions):
        automation = self.create(name=name, description=description, type=type)
        for condition in conditions:
            Condition.objects.create(
                automation=automation,
                name=condition["name"],
                trigger=condition["trigger"],
                value=condition["value"],
                operator=condition["operator"],
            )
        for action in actions:
            Action.objects.create(
                automation=automation,
                name=action["name"],
                action=action["action"],
                target=action["target"],
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
                name=condition["name"],
                trigger=condition["trigger"],
                value=condition["value"],
                operator=condition["operator"],
            )
        for action in actions:
            Action.objects.create(
                automation=automation,
                name=action["name"],
                action=action["action"],
                target=action["target"],
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
    name = models.CharField(max_length=100)
    trigger = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    """
    eq: equal
    ne: not equal
    gt: greater than
    lt: less than
    ge: greater than or equal
    le: less than or equal
    """
    operator = models.CharField(max_length=10)


class Action(models.Model):
    automation = models.ForeignKey(
        Automation, on_delete=models.CASCADE, related_name="actions"
    )
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
