from django.test import TestCase
from passandplay.models import Player


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        self.client.post("/", data={"player_text": "A new character"})
        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.text, "A new character")

    def test_redirects_after_POST(self):
        response = self.client.post(
            "/", data={"player_text": "A new character"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/games/testgame")

    def test_only_saves_players_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Player.objects.count(), 0)


class GamesViewTest(TestCase):
    def test_uses_game_template(self):
        response = self.client.get("/games/testgame")
        self.assertTemplateUsed(response, "passandplaygame.html")

    def test_displays_all_game_characters(self):
        Player.objects.create(text="First character")
        Player.objects.create(text="Second character")

        response = self.client.get("/games/testgame")

        self.assertContains(response, "Player 1")
        self.assertContains(response, "Player 2")


class PlayerModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_player = Player()
        first_player.text = "First player"
        first_player.save()

        second_player = Player()
        second_player.text = "Second Player"
        second_player.save()

        saved_items = Player.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_player = saved_items[0]
        second_saved_player = saved_items[1]
        self.assertEqual(first_saved_player.text, "First player")
        self.assertEqual(second_saved_player.text, "Second Player")
