"""
ASGI config for iot_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import importlib
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iot_server.settings")

websocket_urlpatterns = []

for app in settings.INSTALLED_APPS:
    try:
        routing = importlib.import_module(f"{app}.routing")
        websocket_urlpatterns += getattr(routing, "websocket_urlpatterns", [])
    except ModuleNotFoundError:
        continue

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)
