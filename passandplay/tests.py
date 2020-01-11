from django.test import TestCase
from passandplay.models import Player, Game


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_only_saves_players_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Player.objects.count(), 0)


class GamesViewTest(TestCase):
    def test_uses_game_template(self):
        response = self.client.get("/games/testgame")
        self.assertTemplateUsed(response, "passandplaygame.html")

    def test_displays_all_game_characters(self):
        game = Game.objects.create()
        Player.objects.create(text="First character", game=game)
        Player.objects.create(text="Second character", game=game)

        response = self.client.get("/games/testgame")

        self.assertContains(response, "Player 1")
        self.assertContains(response, "Player 2")


class NewGameTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post("/games/new", data={"player_text": "A new character"})
        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.text, "A new character")

    def test_redirects_after_POST(self):
        response = self.client.post(
            "/games/new", data={"player_text": "A new character"}
        )
        self.assertRedirects(response, "/games/testgame")


class PlayerAndGameModelTest(TestCase):
    def test_saving_and_retrieving_items(self):

        game = Game()
        game.save()

        first_player = Player()
        first_player.text = "First player"
        first_player.game = game
        first_player.save()

        second_player = Player()
        second_player.text = "Second Player"
        second_player.game = game
        second_player.save()

        saved_game = Game.objects.first()
        self.assertEqual(saved_game, game)

        saved_items = Player.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_player = saved_items[0]
        second_saved_player = saved_items[1]
        self.assertEqual(first_saved_player.text, "First player")
        self.assertEqual(first_saved_player.game, game)
        self.assertEqual(second_saved_player.text, "Second Player")
        self.assertEqual(second_saved_player.game, game)
