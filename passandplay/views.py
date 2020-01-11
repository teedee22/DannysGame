from django.shortcuts import redirect, render
from passandplay.models import Player


def home_page(request):
    return render(request, "home.html")


def game_view(request):
    return render(
        request, "passandplaygame.html", {"players": Player.objects.all()}
    )


def new_game(request):
    Player.objects.create(text=request.POST["player_text"])
    return redirect("/games/testgame")
