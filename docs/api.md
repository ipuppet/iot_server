# API

See the swagger documentation at `${my-server-ip}:8090/schema/swagger-ui/` for more information on the API.

## Clarifications

All url parameters of `id` indicate the id of the object to be retrieved, updated, or deleted.

For example, `/automation/automations/{id}/` would be `/automation/automations/1/` to get the automation with id 1.

All id parameters are integers except Device id, which is a UUID.
