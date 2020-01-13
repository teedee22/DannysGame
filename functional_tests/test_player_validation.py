from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class PlayerValidationTest(FunctionalTest):
    def test_cannot_add_empty_players(self):
        # Dannie goes to the home page and tries to submit and empty player
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("player_name").send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that play characters cannot be blank
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_css_selector(".has-error").text,
                "You can't have a blank player name",
            )
        )

        # She tries again with some text for the palyer, which now works.
        self.input_character_name("Mr Blobby")
        self.wait_for_player_number_to_appear_in_table("1")

        # She tries to submit another blank Player
        self.browser.find_element_by_id("player_name").send_keys(Keys.ENTER)

        # She receives another warning
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_css_selector(".has-error").text,
                "You can't have a blank player name",
            )
        )

        # She fills in a second player name
        self.input_character_name("Hagrid")
        self.wait_for_player_to_appear_in_table("2")
