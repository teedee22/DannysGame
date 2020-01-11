from django.db import models


class Game(models.Model):
    pass


class Player(models.Model):
    text = models.TextField(default="")
    game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
