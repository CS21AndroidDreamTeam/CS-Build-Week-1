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
from django.core import serializers
import random
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
    map = list(Room.objects.values())
    return JsonResponse(map, safe=False)


@api_view(["GET"])
def get_item_0(request):
    ran = random.randint(1, 4)
    data = serializers.serialize("json", Item.objects.filter(origin="Prehistoric Cave", originid=ran))
    return JsonResponse(data, safe=False)



@api_view(["GET"])
def get_item_1(request):
    ran = random.randint(1, 9)
    data = serializers.serialize("json", Item.objects.filter(origin="Medieval Wizards Tower", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_2(request):
    ran = random.randint(1, 7)
    data = serializers.serialize("json", Item.objects.filter(origin="Abandoned Cottage", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_3(request):
    ran = random.randint(1, 6)
    data = serializers.serialize("json", Item.objects.filter(origin="Alchemists' Laboratory", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_4(request):
    ran = random.randint(1, 7)
    data = serializers.serialize("json", Item.objects.filter(origin="Viking Barracks", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_5(request):
    ran = random.randint(1, 7)
    data = serializers.serialize("json", Item.objects.filter(origin="Roman Colosseum", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_6(request):
    ran = random.randint(1, 7)
    data = serializers.serialize("json", Item.objects.filter(origin="London Shop", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_7(request):
    ran = random.randint(1, 9)
    data = serializers.serialize("json", Item.objects.filter(origin="Futuristic Lab", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_8(reqeust):
    ran = random.randint(1, 5)
    data = serializers.serialize("json", Item.objects.filter(origin="Barbaric Outpost", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_9(request):
    ran = random.randint(1, 7)
    data = serializers.serialize("json", Item.objects.filter(origin="Western Town", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_10(request):
    ran = random.randint(1, 6)
    data = serializers.serialize("json", Item.objects.filter(origin="Colonial Puritan Church", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_11(request):
    ran = random.randint(1, 5)
    data = serializers.serialize("json", Item.objects.filter(origin="Nazi Meeting Hall", originid=ran))
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_item_12(request):
    ran = random.randint(1, 6)
    data = serializers.serialize("json", Item.objects.filter(origin="Chinese Pagoda", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_13(request):
    ran = random.randint(1, 5)
    data = serializers.serialize("json", Item.objects.filter(origin="Cold War Nuclear Site", originid=ran))
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def get_item_14(request):
    ran = random.randint(1, 8)
    data = serializers.serialize("json", Item.objects.filter(origin="Beached Pirate Ship", originid=ran))
    return JsonResponse(data, safe=False)
