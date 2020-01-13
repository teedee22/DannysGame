from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class PlayerValidationTest(FunctionalTest):
    def test_cannot_add_empty_players(self):
        # Dannie goes to the home page and tries to submit and empty player
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("player_name").send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_css_selector(".has-error").text,
                "You can't have an empty list item",
            )
        )

        # She tries again with some text for the item, which now works.
        self.fail("write me!")
