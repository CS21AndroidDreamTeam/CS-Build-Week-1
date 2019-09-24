from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
from django.db import models
from api.models import Room, Player, Item
import json


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.current_room_csv
    return JsonResponse(
        {'uuid': uuid, 'name': player.user.username, 'title': room.title, 'description': room.description,
         'current_room': room}, safe=True)


@api_view(["GET"])
def get_map(request):
    map = Room.objects.all()
    return JsonResponse(map, safe=False)
