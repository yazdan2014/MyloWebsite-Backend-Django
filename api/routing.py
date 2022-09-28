# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/user/(?P<guild_id>\w+)/$', consumers.ClientConsumer.as_asgi()),
    re_path(r'ws/bot/(?P<token>\w+)/$', consumers.BotConsumer.as_asgi()),
] 