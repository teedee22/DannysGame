from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os

MAX_WAIT = 10


class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = "http://" + staging_server

    def tearDown(self):
        self.browser.quit()

    def wait_for_player_number_to_appear_in_table(self, number):
        start_time = time.time()
        while True:
            try:
                time.sleep(0.1)
                table = self.browser.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(f"Player {number}", rows[len(rows) - 1].text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def input_character_name(self, character_name):
        inputbox = self.browser.find_element_by_id("player_name")
        inputbox.send_keys(character_name)
        inputbox.send_keys(Keys.ENTER)
