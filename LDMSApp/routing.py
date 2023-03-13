from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import DatabaseConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/database/', DatabaseConsumer.as_asgi()),
    ]),
})
