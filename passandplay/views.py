from django.shortcuts import redirect, render
from passandplay.models import Game, Player


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
