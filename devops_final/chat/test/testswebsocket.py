
import unittest
from django.test import TestCase
from channels.testing import WebsocketCommunicator
from django.conf.urls import url
# application = URLRouter([
#     url(r"^testws/(?P<message>\w+)/$", KwargsWebSocketApp.as_asgi()),
# ])
from channels.routing import URLRouter
from django.urls import re_path
from chat import consumers


application = URLRouter([
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
])


class Websockettest(TestCase):



    async def test_Websockettest_connect_and_receive(self):
        communicator = WebsocketCommunicator(application, "/ws/chat/testroom/")
        connected, subprotocol = await communicator.connect()
        assert connected
        # self.assertEqual(connected, None)
        # await communicator.send_to(text_data="hello")
        # response = await communicator.receive_from()
        # self.assertEqual(response == "hello")
        await communicator.disconnect()
    

    async def test_Websockettest_senddata_json(self):
        communicator = WebsocketCommunicator(application, "/ws/chat/testroom/")
        connected, subprotocol = await communicator.connect()
        await communicator.send_json_to({
            "roomname":"testroom",
            "username":"testuser123",
            "message":"Hello World!",
            "command":"new_message"
        })
        response = await communicator.receive_json_from()
        assert response == {
            "message":"Hello World!"
        }
        await communicator.disconnect()       


