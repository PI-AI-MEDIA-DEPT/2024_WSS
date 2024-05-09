from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print("ROOM NAME : ",self.room_name)
        if self.room_name == "pos":
            self.room_group_name = 'pos'
        else:
            self.room_group_name = 'cai'
        #self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("received ..",text_data_json)
        message = text_data_json['message']
        # x = text_data_json['x']
        # y = text_data_json['y']
        # username = text_data_json['username']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                # 'x' : x,
                # 'y' : y
                # 'username': username
            }
        )

    def chat_message(self, event):
        message = event['message']
        # x = event['x']
        # y = event['y']
        # username = event['username']
        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
            # 'x' : x,
            # 'y' : y
            # 'username': username
        }))

    def alarm(self, event):
        message = event['message']
        # username = event['username']
        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
            # 'username': username
        }))

    def pos(self, event):
        message = event['message']
        user1 = event['user1']
        user2 = event['user2']
        # username = event['username']
        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
            'user1' : user1,
            'user2' : user2
        }))

    # def events_alarm(self, event):
    #     self.send_json(
    #         {
    #             'type': 'events.alarm',
    #             'content': event['content']
    #         }
    #     )
