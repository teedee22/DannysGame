from selenium import webdriver
import unittest

browser = webdriver.Firefox()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_game_and_retrieve_it_later(self):

        # Dani wants to play her guess who game with her family without the
        # need for a quiz master. She has heard that she can use a cool new
        # website, she goes to the home page
        self.browser.get("http://localhost:8000")

        # She notices that the game is named after her
        self.assertIn("Danni", self.browser.title)
        self.fail("Finish the test")

        # She is invited to dive straight in and add player 1's name
        # She types 'Henry the Hoover' into a text box

        # When she hits enter, the page updates, and now the page shows
        # player 1 with a confirmation next to it that they she has played
        # and player 2 appears beneath with a text box next to it

        # She passes to her brother, who enters 'Pingu' into the textbox and
        # hits enter

        # The page updates again, showing player 1 and player 2 have entered
        # their player names and the game is now waiting for player 3

        # Danni wonders whether the site will remember the game, because her
        # dad, the third player is busy at the moment. She notices the site has
        # generated a unique URL for her which she can revisit at any time.

        # She visits the URL on her phone and notices the game is still there,
        # waiting for player 3's input.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
