# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver
# import json
# import os
#
# SCREEN_DUMP_LOCATION = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), 'screendumps'
# )
#
#
# class SchedulerViewsTests(StaticLiveServerTestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()
#
#     def test_rest_zonemap_render_page(self):
#         self.selenium.get(f"{self.live_server_url}/zones/?format=json")
#         self.selenium.save_screenshot(f"{SCREEN_DUMP_LOCATION}/test_rest_zonemap_render_page.png")
#         json_data = json.loads(self.selenium.find_element_by_tag_name('body').text)
#
#         self.assertIn('"num": 1', json_data)

