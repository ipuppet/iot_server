from django.db import models


class Automation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10)  # and, or


class Condition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
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
    name = models.CharField(max_length=100)
    description = models.TextField()
    action = models.CharField(max_length=100)
    target = models.CharField(max_length=100)


class AutomationCondition(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)


class AutomationAction(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
