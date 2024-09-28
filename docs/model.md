# Model

## Devices

### Device

- id: UUID
- name
- description
- type: "condition" | "action"
- fields: [[Device Field]](#device-field)

For condition devices, the fields are the conditions that the device will check. For example, a temperature sensor device will have a field named `Temperature` with value `temperature`, name is for display purposes only, and the value is the `field` of the device data.
For action devices, the fields are the infrared codes that the device can send. For example, a TV device will have a field named `Power` with value `specific-infrared-code`.

### Device Field

- device: [Device](#device)
- name
- value

PK: `unique_together = ["device", "name", "value"]`

### Device Data

- id
- device: [Device](#device)
- field
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
