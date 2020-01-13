from django.test import TestCase
from passandplay.models import Player, Game


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
