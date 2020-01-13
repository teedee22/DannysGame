from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

MAX_WAIT = 10


class NewVisitorTest(FunctionalTest):
    def input_character_name(self, character_name):
        inputbox = self.browser.find_element_by_id("player_name")
        inputbox.send_keys(character_name)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_game_and_add_players(self):

        # Dannie wants to play her guess who game with her family without the
        # need for a quiz master. She has heard that she can use a cool new
        # website, she goes to the home page
        self.browser.get(self.live_server_url)

        # She notices that the game is named after her
        self.assertIn("Dannie", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Dannie's Game", header_text)

        # She is invited to dive straight in and add player 1's name
        player_text = self.browser.find_element_by_tag_name("h3").text
        self.assertIn("Player 1", player_text)
        inputbox = self.browser.find_element_by_id("player_name")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter your player's character name",
        )

        # She types 'Henry the Hoover' into a text box
        inputbox.send_keys("Henry the Hoover")

        # When she hits enter, the page updates, and now the page shows
        # player 1 with a confirmation next to it that they she has played
        # and player 2 appears above with a text box next to it
        inputbox.send_keys(Keys.ENTER)

        self.wait_for(
            lambda: self.assertIn(
                self.browser.find_element_by_tag_name("h3").text, "Player 2",
            )
        )

        # She passes to her brother, who enters 'Pingu' into the textbox and
        # hits enter
        self.input_character_name("Pingu")

        # The page updates again, showing player 1 and player 2 have entered
        self.wait_for_row_in_list_table("2")
        # The page shows it is waiting for player 3's input
        self.wait_for(
            lambda: self.assertIn(
                self.browser.find_element_by_tag_name("h3").text, "Player 3",
            )
        )

    def test_multiple_users_can_start_new_games_at_different_urls(self):
        self.browser.get(self.live_server_url)

        # Dannie starts a new Game
        self.input_character_name("Henry the Hoover")
        self.wait_for_row_in_list_table("1")

        # She passes to her brother
        self.input_character_name("Pingu")
        self.wait_for_row_in_list_table("2")
        # She wonders whether the site will remember the game, because her
        # dad, the third player is busy at the moment. She notices the site has
        # generated a unique URL for her which she can revisit at any time.

        dannie_game_url = self.browser.current_url
        self.assertRegex(dannie_game_url, "/games/.+")

        # Now a new user, her uncle Bob, comes along to the website

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Bob visits the home page. There is no sign of Dannie and her
        # brother's game

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Henry", page_text)
        self.assertNotIn("Pingu", page_text)

        # Bob starts a new game by entering a new player
        self.input_character_name("The Queen")
        self.wait_for_row_in_list_table("1")

        # Bob gets his own unique URL
        bob_game_url = self.browser.current_url
        self.assertRegex(bob_game_url, "games/.+")
        self.assertNotEqual(bob_game_url, dannie_game_url)

        # There is no trace of Dannie's game
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Pingu", page_text)

    def test_user_can_play_game(self):
        self.browser.get(self.live_server_url)

        # Dannie starts a new Game and enters the first player
        self.input_character_name("Henry the hoover")
        self.wait_for_row_in_list_table("1")

        # She passes over to her brother who enters the second player
        self.input_character_name("Pingu")
        self.wait_for_row_in_list_table("2")

        # He passes to Dannie's father who enters the third character
        self.input_character_name("Voldermort")
        self.wait_for_row_in_list_table("3")

        # Player 4 appears beneath with a text box next to it.
        self.wait_for(
            lambda: self.assertIn(
                self.browser.find_element_by_tag_name("h3").text, "Player 4",
            )
        )

        # she notices that there is a button to start the game. She presses it.
        startbutton = self.browser.find_element_by_id("start_button")
        startbutton.send_keys(Keys.ENTER)

        # After pressing the button, the game shows the four players in a
        # random order On the screen. She closes her browser and goes back
        # to the unique URL
        self.wait_for(
            lambda: self.assertIn(
                "Henry", self.browser.find_element_by_tag_name("body").text
            )
        )
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertIn("Voldermort", page_text)
        self.assertIn("Pingu", page_text)
