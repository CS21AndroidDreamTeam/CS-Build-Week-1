from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    positionx = models.IntegerField()
    positiony = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=200)
    positionx = models.IntegerField()
    positiony = models.IntegerField()



class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
