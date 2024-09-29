# Docs

## Models

[models](model.md)

## API

See the swagger documentation at `${my-server-ip}:8090/schema/swagger-ui/` for more information on the API.

### Clarifications

All url parameters of `id` indicate the id of the object to be retrieved, updated, or deleted.

For example, `/automation/automations/{id}/` would be `/automation/automations/1/` to get the automation with id 1.

All id parameters are integers except Device id, which is a UUID.

## Add data to server

Path: `/device/devices/{id}/data/`
Method: POST
Body: json

### Example

Post data to device `A20D1CBE-78A3-41AF-9A61-D5243914A0E6`:

Path: `/device/devices/A20D1CBE-78A3-41AF-9A61-D5243914A0E6/data/`

```json
{
  "field": "temperature",
  "value": 30
}
```

Response:

```json
{
    "field": "temperature",
    "value": "30",
    "timestamp": "2024-09-29T18:43:49.405743Z"
}
```

If an automation is triggered, the response will include the triggered automation's infrared signals.

```json
{
    "field": "temperature",
    "value": "30",
    "timestamp": "2024-09-29T18:43:49.405743Z",
    "infrareds": [
        "2222222",
        "2222222"
    ]
}
```

## Infrared Signal

### Step 1: User action

If user wants to add a new device controller (devices that can be controlled by the infrared signal), user needs to clicks `add device` button on the frontend.

### Step 2: Frontend action

Then, the frontend will show a form to the user to fill in the device name and an empty list (with a `plus` button) for adding the infrared signal.

### Step 3: User action

User needs to press the `plus` button to add a new field to the list. The field will be a pair of `name` and `value`, where `name` is the name of the field, e.g. `On`, and `value` is the value of the infrared signal, e.g. `0x12345678`.

### Step 4: Frontend action

After the user clicks the `plus` button, frontend will start a WebSocket connection to the backend and wait for the infrared signal from the backend.

Give a note to the user that the user needs to press the physical button on the board to receive the infrared signal.

### Step 5: Dev board action

After the user presses the button on the board, it will start waiting for the infrared signal, and start a WebSocket connection to the backend. It will be better if the board can show a message (or a LED) to the user that the board is ready to receive the signal.

When the board receives the infrared signal, it will send the signal to the backend, after the backend receives the signal, it will close the WebSocket connection.

### Step 6: User action

After the board ready to receive the signal, the user needs to press the button on the remote control to send the signal to the board.

### Step 7: Frontend action

After receiving the signal from the backend, the frontend will fill the `value` field with the received signal.

### More fields

User can add more fields by pressing the `plus` button again, and repeat the steps 4-7.

After the user finishes adding the fields, the user can press the `save` button to save the device controller to the server, and the frontend will close the WebSocket connection.
