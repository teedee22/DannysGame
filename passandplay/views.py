from django.shortcuts import redirect, render
from passandplay.models import Player


def home_page(request):
    if request.method == "POST":
        Player.objects.create(text=request.POST["player_text"])
        return redirect("/")
    return render(request, "home.html", {"players": Player.objects.all()})
