# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/guild/(?P<guild_name>\w+)/$', consumers.EchoConsumer.as_asgi()),
     re_path(r'ws/bot/(?P<token>\w+)/$', consumers.EchoConsumer.as_asgi()),
]