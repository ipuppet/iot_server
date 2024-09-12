# Model

## Devices

### Device

- id
- name
- description
- type: "condition" | "action"
- fields: [[Device Field]](#device-field)

For condition devices, the fields are the conditions that the device will check. For example, a temperature sensor device will have a status field `temperature` that indicates the current temperature.

For action devices, the fields are the actions that the device will perform. For example, a light device will have control fields `on` and `off` that will be send to the device to turn it on or off. It can also have a status field `brightness` with a value between `0` and `100` that indicates the brightness of the light.

### Device Field

- id
- device: [Device](#device)
- name
- type: "status" | "control"
- target: path of the field in the device data, for control fields it is the command to send to the device

### Device Data

- id
- device: [Device](#device)
- name
- value
- timestamp

## Automations

### Automation

- id
- name
- description
- created_at
- updated_at
- type: "and" | "or"
- conditions: [[Condition]](#condition)
- actions: [[Action]](#action)

For `and` automations, all conditions must be met for the actions to be executed. For `or` automations, at least one condition must be met for the actions to be executed.

### Condition

- id
- device: [Device](#device)
- field: [Device Field](#device-field)
- value
- operator: "eq" | "ne" | "gt" | "lt" | "ge" | "le"

### Action

- id
- device: [Device](#device)
- field: [Device Field](#device-field)
