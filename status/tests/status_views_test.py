from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.conf import settings
import os

SCREEN_DUMP_LOCATION = os.path.join(
    settings.BASE_DIR, 'screendumps'
)


class StatusViewsTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_landing_page_title(self):
        self.selenium.get(f"{self.live_server_url}")
        self.selenium.save_screenshot(f"{SCREEN_DUMP_LOCATION}/test_landing_page_title.png")

        self.assertIn('Sprinkler Controller ][', self.selenium.title)
