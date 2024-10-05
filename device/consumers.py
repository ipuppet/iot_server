import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DeviceConsumer(AsyncWebsocketConsumer):
    isDevice = False

    async def connect(self):
        self.room_group_name = "infrared_control"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        if "ws/device" in self.scope["path"]:
            self.isDevice = True
        else:
            self.isDevice = False

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        signal = data["signal"]
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "forward_signal", "signal": signal}
        )

    async def forward_signal(self, event):
        if self.isDevice:
            return
        signal = event["signal"]
        await self.send(text_data=json.dumps({"signal": signal}))

    async def run_signal(self, event):
        if not self.isDevice:
            return
        signal = event["signal"]
        await self.send(text_data=json.dumps({"signal": signal}))
