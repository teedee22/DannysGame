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
        game = Game.objects.create()
        response = self.client.get(f"/games/{game.id}/")
        self.assertTemplateUsed(response, "passandplaygame.html")

    def test_displays_only_players_in_current_game(self):
        correct_game = Game.objects.create()
        Player.objects.create(text="First character", game=correct_game)
        Player.objects.create(text="Second character", game=correct_game)
        other_game = Game.objects.create()
        Player.objects.create(
            text="Other game First character", game=other_game
        )
        Player.objects.create(
            text="Other game Second character", game=other_game
        )
        Player.objects.create(
            text="Other game Third character", game=other_game
        )
        Player.objects.create(
            text="Other game Fourth character", game=other_game
        )

        response = self.client.get(f"/games/{correct_game.id}/")

        self.assertContains(response, "Player 1")
        self.assertContains(response, "Player 2")
        self.assertNotContains(response, "Player 4")

    def test_passes_correct_game_to_template(self):
        other_game = Game.objects.create()
        correct_game = Game.objects.create()
        response = self.client.get(f"/games/{correct_game.id}/")
        self.assertEqual(response.context["game"], correct_game)


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
        new_game = Game.objects.first()
        self.assertRedirects(response, f"/games/{new_game.id}/")


class NewPlayerTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_game(self):
        other_game = Game.objects.create()
        correct_game = Game.objects.create()

        self.client.post(
            f"/games/{correct_game.id}/add_player",
            data={"player_text": "Spongebob"},
        )

        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.text, "Spongebob")
        self.assertEqual(new_player.game, correct_game)

    def test_redirects_to_game_view(self):
        other_game = Game.objects.create()
        correct_game = Game.objects.create()

        response = self.client.post(
            f"/games/{correct_game.id}/add_player",
            data={"player_text": "Spongebob"},
        )

        self.assertRedirects(response, f"/games/{correct_game.id}/")


class StartGameTest(TestCase):
    def test_uses_start_game_template(self):
        game = Game.objects.create()
        Player.objects.create(text="one", game=game)
        Player.objects.create(text="two", game=game)
        Player.objects.create(text="three", game=game)

        response = self.client.get(f"/games/{game.id}/start_game")

        self.assertTemplateUsed(response, "startgame.html")

    def test_game_displays_all_characters(self):
        game = Game.objects.create()
        Player.objects.create(text="one", game=game)
        Player.objects.create(text="two", game=game)
        Player.objects.create(text="three", game=game)

        response = self.client.get(f"/games/{game.id}/start_game")

        self.assertContains(response, "one")
        self.assertContains(response, "two")
        self.assertContains(response, "three")


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
