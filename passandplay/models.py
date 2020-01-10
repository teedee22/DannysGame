from django.db import models


class Player(models.Model):
    text = models.TextField(default="")
