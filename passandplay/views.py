from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # if request.method == "POST":
    return render(
        request,
        "home.html",
        {"new_player_text": request.POST.get("player_text", "")},
    )
    # return render(request, "home.html")
