"""dannysgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from passandplay import views
from django.urls import path

urlpatterns = [
    path("", views.home_page, name="home"),
    path("games/<int:game_id>/", views.game_view, name="game_view"),
    path(
        "games/<int:game_id>/add_player", views.add_player, name="add_player"
    ),
    path("games/new", views.new_game, name="new_game"),
]
