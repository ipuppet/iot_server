import json
from channels.generic.websocket import AsyncWebsocketConsumer


class WebConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "infrared_control"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # No message handling is needed for the web client
        pass

    async def send_signal(self, event):
        signal = event["signal"]
        await self.send(text_data=json.dumps({"signal": signal}))


class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "infrared_control"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        signal = data["signal"]

        # Send the infrared signal to the web client
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "send_signal", "signal": signal}
        )
