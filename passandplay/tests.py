from django.test import TestCase
from passandplay.models import Player


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            "/", data={"player_text": "A new character"}
        )
        self.assertIn("Player 1", response.content.decode())
        self.assertTemplateUsed(response, "home.html")


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
