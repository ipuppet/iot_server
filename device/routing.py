from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/web/$", consumers.DeviceConsumer.as_asgi()),
    re_path(r"ws/device/$", consumers.DeviceConsumer.as_asgi()),
]
