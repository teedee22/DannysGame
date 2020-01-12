from .base import FunctionalTest

MAX_WAIT = 10


class LayoutAndStyling(FunctionalTest):
    def test_layout_and_styling(self):
        # Dannie goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the inbox box is centered
        inputbox = self.browser.find_element_by_id("player_name")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2, 512, delta=10
        )
