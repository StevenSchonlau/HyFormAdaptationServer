# design/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing
from django.conf.urls import url
from chat.consumers import ChatConsumer
from api.consumers import APIConsumer
from ai.consumers import TaskConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            #chat.routing.websocket_urlpatterns
            url(r'ws/chat/$', ChatConsumer),
            url(r'ws/api/$', APIConsumer),
            url(r'ws/tasks/$', TaskConsumer)
        ])
    ),
})
