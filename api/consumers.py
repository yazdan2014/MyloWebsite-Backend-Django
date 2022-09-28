from cgitb import text
from email import message
from pickle import TRUE
from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from .models import BotTokens

class ClientConsumer(WebsocketConsumer):
    def websocket_connect(self, event):
        self.user = self.scope["user"]
        if self.user:
            # discord_info = self.get_discord_info()
            self.guildId = self.scope['url_route']['kwargs']['guild_id']
            async_to_sync(self.channel_layer.group_add)(self.guildId, self.channel_name)

            async_to_sync(self.channel_layer.group_send)("bot", {
                "type":"message.send",
                "message":json.dumps({"type":"newDashboard", "guildId":self.guildId})
            })

            self.accept()
        else:
            self.close()

    def websocket_receive(self, event):
        text_data = event.get('text', None)
        message = json.loads(text_data)
        print(message)
        if message['type'] == "forceskip":
            async_to_sync(self.channel_layer.group_send)("bot", {
                "type":"message.send",
                "message":json.dumps({"type":"command", "command":"forceskip", "guildId":message['guildId']})
            })
        
        elif message['type'] == "unpause":
            async_to_sync(self.channel_layer.group_send)("bot", {
                "type":"message.send",
                "message":json.dumps({"type":"command", "command":"unpause", "guildId":message['guildId']})
            })
        
        elif message['type'] == "pause":
            async_to_sync(self.channel_layer.group_send)("bot", {
                "type":"message.send",
                "message":json.dumps({"type":"command", "command":"pause", "guildId":message['guildId']})
            })
        # if text['type'] == "bot_response":



        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })

    def get_discord_info(self):
        return {"dicord_id": "dicord_user_id", "guildId": "696297810462769222"}


    def websocket_disconnect(self, close_code):
        pass
        # self.channel_layer.group_discard(self.guild, self.channel_name)
        # raise StopConsumer

    def message_send(self, event):        
        print(event)
        self.send(event["message"])

class BotConsumer(WebsocketConsumer):
    def connect(self):
        # self.token = self.scope['url_route']['kwargs']['token']
        # res = self.authenticate_bot(self.token)
        if True:
            async_to_sync(self.channel_layer.group_add)("bot", self.channel_name)
            self.accept()
 
        else:
            self.send({'type': 'websocket.close', })        
    def receive(self, text_data):
        message = json.loads(text_data)
        
        if message["type"] == "status":
            if message['status'] == 'playing':
                async_to_sync(self.channel_layer.group_send)(message['guildId'], {
                    "type":"message.send",
                    "message":json.dumps({"type":"status", "status":"playing", "metadata":message['metadata']})
                })
            if message['status'] == "idle":
                async_to_sync(self.channel_layer.group_send)(message['guildId'], {
                    "type":"message.send",
                    "message":json.dumps({"type":"status", "status":"idle"})
                })

        # text_data = event.get('text', None)
        # message = json.loads(text_data)
        # print(message)
        # if text['type'] == "bot_response":

 
 
        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })
 
    def disconnect(self, close_code):  
        self.channel_layer.group_discard('bot', self.channel_name)
        raise StopConsumer

    def message_send(self, event):
        self.send(text_data=event["message"])

    def authenticate_bot(token):
        try:
            BotTokens.objects.get(token=token)
            return True
        except BotTokens.DoesNotExist:
            return False