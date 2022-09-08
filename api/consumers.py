from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
import json
from .models import BotTokens

class ClientConsumer(SyncConsumer):
    def websocket_connect(self):
            self.user = self.scope["user"]
            if self.user:
                discord_info = self.get_discord_info()
                self.guild = discord_info["guild"]
                self.channel_layer.group_add(
                    self.guild,
                    self.channel_name
                )

                self.send({
                    "type": "websocket.accept",
                })
            else:
                self.send({'type': 'websocket.close', })

          
        

    def websocket_receive(self, event):


        text = event["text"]

        # if text['type'] == "bot_response":



        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })

    def get_discord_info():
        return {"dicord_id": "dicord_user_id", "guild": "guild_name"}


    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.guild, self.channel_name)
        raise StopConsumer

class BotConsumer(SyncConsumer):
    def websocket_connect(self):
        self.token = self.scope['url_route']['kwargs']['token']
        res = self.authenticate_bot(self.token)
        if res:
              self.channel_layer.group_add("bot", self.channel_name)
              self.send({
                    "type": "websocket.accept",
                })
        else:
            self.send({'type': 'websocket.close', })
          
        

    def websocket_receive(self, event):


        text = event["text"]

        # if text['type'] == "bot_response":



        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })

    def disconnect(self, close_code):
        self.channel_layer.group_discard('bot', self.channel_name)
        raise StopConsumer

    def authenticate_bot(token):
        try:
            BotTokens.objects.get(token=token)
            return True
        except BotTokens.DoesNotExist:
            return False