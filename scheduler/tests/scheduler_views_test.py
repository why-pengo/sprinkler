from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import requests
import os

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "screendumps"
)


class SchedulerViewsTests(StaticLiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_rest_zonemap_api_call(self):
        response = requests.get(f"{self.live_server_url}/zones/?format=json")

        self.assertEqual(200, response.status_code)
