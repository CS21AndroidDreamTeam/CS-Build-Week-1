from django.db import models
import uuid


# Create your models here.
class Room(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    positionx = models.IntegerField()
    positiony = models.IntegerField()


class Player(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)
    positionx = models.IntegerField()
    positiony = models.IntegerField()
    current_room_csv = models.CharField(max_length=10, default="1,1")


class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
