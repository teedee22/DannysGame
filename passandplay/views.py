from django.shortcuts import redirect, render
from passandplay.models import Game, Player


def home_page(request):
    return render(request, "home.html")


def game_view(request):
    return render(
        request, "passandplaygame.html", {"players": Player.objects.all()}
    )


def new_game(request):
    game = Game.objects.create()
    Player.objects.create(text=request.POST["player_text"], game=game)
    return redirect("/games/testgame")
