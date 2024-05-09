import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from django.shortcuts import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from channels import Group
from django.views.decorators.csrf import csrf_exempt
def index(request):
    """Главная страница"""
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    """"""
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def room(request, room_name):
    """"""
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

# #chat\consumers.py
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'cai' #Change
#         #self.room_group_name = 'chat_%s' % self.room_name

#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accep

# def receive(self, text_data):
#     text_data_json = json.loads(text_data)
#     print("received ..",text_data_json)
#     message = text_data_json['message']
#     # username = text_data_json['username']


# from channels.layers import get_channel_layer
# from django.shortcuts import HttpResponse
def posData(req):
    data = {"",}
    return HttpResponse('<p>Done</p>')
@csrf_exempt
def alarm(req):
    print("alarm")
    channel_layer = get_channel_layer()
    ms = json.loads(req.body)
    async_to_sync(channel_layer.group_send)(
        'cai',
        {
            'type': 'alarm',
            'message': ms
        }
    )

    return HttpResponse('<p>Done</p>')
@csrf_exempt
def pos(req):
    if req.method == 'POST':
        user1 = req.POST.get("user1")
        user2 = req.POST.get("user2")
        print(req.body)
        data = json.loads(req.body)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'cai',
        {
            'type': 'pos',
            "user1" : data['user1'],
            "user2": data['user2'],
            'message': 'pos'
        }
    )

    return HttpResponse('<p>Done</p>')