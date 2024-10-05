from . import models, serializers

from device.models import DeviceField, DeviceData


class Data:
    data = {}

    def __init__(self):
        self.data = {}

    def get(self, device, field):
        if device not in self.data:
            self.data[device] = {}
        if field not in self.data[device]:
            self.data[device][field] = Data.get_latest_data(device, field)
        return self.data[device][field]

    @staticmethod
    def get_latest_data(device, field):
        data = (
            DeviceData.objects.filter(
                device=device,
                field=models.getField(device, {"value": field}, True),
            )
            .order_by("-timestamp")
            .first()
        )

        return data.value if data else None


class Automation:
    def __init__(self, id=-1, automation=None, data=None):
        self.data = data
        if automation:
            self.automation = automation
        elif id != -1:
            self.automation = models.Automation.objects.get(id=id)

        self.conditions = self.automation["conditions"]
        self.actions = self.automation["actions"]
        self.type = self.automation["type"]

    def check_condition(self, condition):
        device = condition["device"]
        field = condition["field"]
        value = condition["value"]
        operator = condition["operator"]
        data = self.data.get(device, field)

        try:
            data = float(data)
            value = float(value)
        except (ValueError, TypeError):
            return False

        if operator == "eq":
            return data == value
        elif operator == "ne":
            return data != value
        elif operator == "gt":
            return data > value
        elif operator == "lt":
            return data < value
        elif operator == "ge":
            return data >= value
        elif operator == "le":
            return data <= value
        return False

    def check(self):
        for condition in self.conditions:
            if self.check_condition(condition):
                if self.type == "or":
                    return True
            else:
                if self.type == "and":
                    return False
        return self.type == "and"

    def get_infrareds(self):
        infrareds = []
        for action in self.actions:
            infrared = DeviceField.objects.get(
                device=action["device"], name=action["field"]
            ).value
            infrareds.append(infrared)
        return infrareds


class AutomationManager:
    def __init__(self):
        self.data = Data()
        self.automations = [
            Automation(
                automation=serializers.AutomationSerializer(automation).data,
                data=self.data,
            )
            for automation in models.Automation.objects.all()
        ]
        pass

    def check_automations(self):
        infrareds = []
        for automation in self.automations:
            if automation.check():
                infrareds.extend(automation.get_infrareds())
        return infrareds
