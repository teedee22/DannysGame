from django.shortcuts import redirect, render
from passandplay.models import Game, Player

import random


def home_page(request):
    return render(request, "home.html")


def game_view(request, game_id):
    game = Game.objects.get(id=game_id)
    players = Player.objects.filter(game=game)
    return render(
        request, "passandplaygame.html", {"players": players, "game": game}
    )


def new_game(request):
    game = Game.objects.create()
    Player.objects.create(text=request.POST["player_text"], game=game)
    return redirect(f"/games/{game.id}/")


def add_player(request, game_id):
    game = Game.objects.get(id=game_id)
    Player.objects.create(text=request.POST["player_text"], game=game)
    return redirect(f"/games/{game.id}/")


def start_game(request, game_id):
    """
    Gets the queryset of players in given game and returns random ordered list
    """
    game = Game.objects.get(id=game_id)
    playerset = Player.objects.filter(game=game)
    players = list(player.text for player in playerset)
    playersrandom = random.sample(players, len(players))
    return render(request, "startgame.html", {"playersrandom": playersrandom})


def rules(request):
    return render(request, "rules.html")
